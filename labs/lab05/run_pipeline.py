from queue import Queue
import argparse
import json
import queue
import sys
import time
from datetime import datetime, timezone
import uuid
from pathlib import Path

from pirlib import sampler
from pirlib.interpreter import PirInterpreter
from pirlib.sampler import PirSampler
import threading



def create_run_id() -> str:
    '''generates a unique run ID using UUID4'''
    run_id = str(uuid.uuid4())
    return run_id

def utc_now_iso() -> str:
	'''Get the current UTC time as an ISO 8601 string with milliseconds precision.'''
	return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def epoch_to_utc_iso(epoch_seconds: float) -> str:
	'''Convert epoch seconds to ISO 8601 UTC string with milliseconds precision.'''
	return datetime.fromtimestamp(epoch_seconds, tz=timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="PIR event logger (JSONL)")
	parser.add_argument("--context", default="models/context.jsonld")
	parser.add_argument("--device-id", required=True)
	parser.add_argument("--wastebin-id", default="urn:dev:team-06:wastebin-01")
	parser.add_argument("--environment-id", default="urn:dev:team-06:environment-01")
	parser.add_argument("--pin", type=int, required=True)
	parser.add_argument("--sample-interval", type=float, default=0.1)
	parser.add_argument("--cooldown", type=float, default=0.0)
	parser.add_argument("--min-high", type=float, default=0.0)
	parser.add_argument("--duration", type=float, default=60.0)
	parser.add_argument("--out", required=True)
	parser.add_argument("--queue-size", type=int, default=10)
	parser.add_argument("--consumer-delay", type=float, default=0.0)
	parser.add_argument("--verbose", action="store_true")
	
	return parser.parse_args()

def validate_args(args):
    '''Validate the parsed command-line arguments and exit with an error message if any validation fails.'''
    # exit code 2 for invalid command-line arguments, exit code 1 for runtime errors (e.g. file I/O errors)
    if args.pin < 0:
        raise ValueError("--pin must be >= 0")
    if args.sample_interval <= 0:
        raise ValueError("--sample-interval must be > 0")
    if args.cooldown < 0:
        raise ValueError("--cooldown must be >= 0")
    if args.min_high < 0:
        raise ValueError("--min-high must be >= 0")
    if args.duration <= 0:
        raise ValueError("--duration must be > 0")
    if args.queue_size <= 0:
        raise ValueError("--queue-size must be > 0")
    if args.consumer_delay < 0:
        raise ValueError("--consumer-delay must be >= 0")
    

def append_jsonl_newline(path: Path) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write("\n")

def append_jsonl_line(path: Path, record: dict) -> None:
    # One JSON object per line, append-only
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

def normalize_entity_id(value: str, default_prefix: str = "urn:dev:team-06:") -> str:
	if value.startswith("urn:"):
		return value
	return f"{default_prefix}{value}"


def create_event(
	event_time: str,
	device_id: str,
	wastebin_id: str,
	environment_id: str,
	event_type: str,
	seq: int,
	run_id: str,
	motion_state: str,
	context_iri: str,
) -> dict:
    '''Create a single event record dictionary based on the provided parameters.'''
    record = {
		"@context": context_iri,
		"@type": "sosa:Observation",
        "event_time" : event_time,
		"device_id" : normalize_entity_id(device_id),
		"wastebin_id" : normalize_entity_id(wastebin_id),
		"environment_id" : normalize_entity_id(environment_id),
		"event_type" : event_type,
		"motion_state" : motion_state,
		"seq" : seq,
		"run_id" : run_id
    }
    return record


def consumer_loop(record_q: Queue, stop_flag: dict, metrics: dict, out_path: Path, consumer_delay: float, verbose: bool):	# args=(event_q, args.out, args, metrics, stop_flag)
	# args=(event_q, args.out, metrics, stop_flag, consumer_delay),
	with out_path.open("a", encoding="utf-8") as f:
		while not stop_flag["stop"] or not record_q.empty():
			try:
				record = record_q.get(timeout=0.5)
			except queue.Empty:
				continue
			except Exception as exc:
				print(f"[consumer] queue get error: {exc}", file=sys.stderr)
				continue

			ingest_time = utc_now_iso()  # time when we consume the event and write to file
			record["ingest_time"] = ingest_time
			# Parse event and ingest times to datetime objects.
			parsed_event_time = datetime.fromisoformat(record["event_time"].replace("Z", "+00:00"))
			parsed_ingest_time = datetime.fromisoformat(ingest_time.replace("Z", "+00:00"))
			record["pipeline_latency_ms"] = (parsed_ingest_time - parsed_event_time).total_seconds() * 1000

			f.write(json.dumps(record) + "\n")
			f.flush()
			metrics["consumed"] += 1
			if verbose:
				print(
					f"[consumer] wrote seq={record['seq']} "
					f"latency_ms={record['pipeline_latency_ms']:.3f}",flush = True
				)
			# monitor the queue size to see how full it gets during execution, which can help identify bottlenecks or capacity issues in the pipeline
			#current_q = record_q.qsize()
			#metrics["max_queue"] = max(metrics["max_queue"], current_q)
			# mark the queue task as done 
			record_q.task_done()
			# if we have consumer delay, sleep for that delay to simulate processing time
			if consumer_delay > 0:
				time.sleep(consumer_delay)
		append_jsonl_newline(out_path) # add a newline at the end of the file for cleanliness after we're done consuming all records
	
      
def producer_loop(args, stop_flag: dict, event_q: Queue, metrics: dict, sampler: PirSampler, interp: PirInterpreter):
	# args=(event_q, sampler, interp, args, metrics, stop_flag)
	run_id = create_run_id() 
	seq = 0

	while not stop_flag["stop"]:
		 # while the duration has not elapsed and no stop signal from Ctrl-C
		try:
			now = time.time()
			raw = sampler.read() # read the raw sensor value (e.g. 0 or 1 for PIR)
		except Exception as exc:
			print(f"[producer] sensor read error: {exc}", file=sys.stderr)
			continue

		for event in interp.update(raw, now):
			seq += 1
			event_time = epoch_to_utc_iso(event["t"]) 

			record = create_event(
					event_time = event_time,
					device_id = args.device_id,
					wastebin_id = args.wastebin_id,
					environment_id = args.environment_id,
					event_type = "motion",
					motion_state = "detected",
					seq = seq,
					run_id = run_id,
					context_iri = args.context,
				)
			try:
				event_q.put_nowait(record) # puts without blocking until queue is full
				# i want the expection to be able to be raised to regulate the behavior 
				metrics["produced"] += 1
				current_q = event_q.qsize()
				metrics["max_queue"] = max(metrics["max_queue"], current_q)

				if args.verbose:
					# print: [producer] queued seq=1 state=detected event_time=2024-06-01T12:00:00.000Z
					print(f"[producer] queued seq={seq} state={record['motion_state']} event_time={event_time}",flush = True)


			except queue.Full:
				metrics["dropped"] += 1
				if args.verbose:
					# print: [producer] queue full, dropped seq=1
					print(f"[producer] queue full, dropped seq={seq}", file=sys.stderr)
		time.sleep(args.sample_interval)

		

def main() -> int:
	args = parse_args()
	validate_args(args)   
	
	event_q = Queue(maxsize=args.queue_size)
	
	metrics = {
		"produced": 0,
		"consumed": 0,
		"dropped": 0,
		"max_queue": 0,
	}

	stop_flag = {"stop": False}

	try:
		sampler = PirSampler(args.pin)
		interp = PirInterpreter(cooldown_s=args.cooldown, min_high_s=args.min_high)

		if args.verbose:
			print(
				f"[logger] device={args.device_id} pin={args.pin} interval={args.sample_interval}s "
				f"cooldown={args.cooldown}s min_high={args.min_high}s duration={args.duration}s out={args.out}",flush = True
			)

		producer_t = threading.Thread(
			target=producer_loop,
			args=(args, stop_flag, event_q, metrics, sampler, interp),
			daemon=True,
		)

		consumer_t = threading.Thread(
			target=consumer_loop,	
			args=(event_q, stop_flag, metrics, Path(args.out), args.consumer_delay ,args.verbose),
			daemon=True,
		)

		producer_t.start()
		consumer_t.start()

		start_t = time.time()

		try:
			while (time.time() - start_t) < args.duration:
				if args.verbose:
					print(
						f"[status] produced={metrics['produced']} "
						f"consumed={metrics['consumed']} "
						f"dropped={metrics['dropped']} "
						f"queue={event_q.qsize()} "
						f"max_queue={metrics['max_queue']}",flush = True
					)
				time.sleep(1.0)
		except KeyboardInterrupt:
			print("\n[main] Ctrl-C: stopping...")
		finally:
			stop_flag["stop"] = True
			producer_t.join()
			consumer_t.join()


	except Exception as exc:
		print(f"[logger] runtime error: {exc}", file=sys.stderr)
		return 1

	print(
        f"[logger] done. produced={metrics['produced']} "
        f"consumed={metrics['consumed']} "
        f"dropped={metrics['dropped']} "
        f"max_queue={metrics['max_queue']}"
    )

	return 0

if __name__ == "__main__":
	raise SystemExit(main())
