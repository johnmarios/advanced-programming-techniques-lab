from queue import Queue
import argparse
import json
import queue
import sys
import time
from datetime import datetime, timezone
import uuid
from pathlib import Path

from labs.lab03.pirlib import sampler
from pirlib.interpreter import PirInterpreter
from pirlib.sampler import PirSampler




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
	parser.add_argument("--device-id", required=True)
	parser.add_argument("--pin", type=int, required=True)
	parser.add_argument("--sample-interval", type=float, default=0.1)
	parser.add_argument("--cooldown", type=float, default=0.0)
	parser.add_argument("--min-high", type=float, default=0.0)
	parser.add_argument("--duration", type=float, default=60.0)
	parser.add_argument("--out", required=True)
	parser.add_argument("--queue-size", type=int, default=10)
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
    

def append_jsonl_newline(path: Path) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write("\n")

def append_jsonl_line(path: Path, record: dict) -> None:
    # One JSON object per line, append-only
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

def create_event(event_time: str, device_id: str, event_type: str, seq: int, run_id: str, motion_state: str) -> dict:
    '''Create a single event record dictionary based on the provided parameters.'''
    record = {
        "event_time" : event_time,
		"device_id" : device_id,
		"event_type" : event_type,
		"motion_state" : motion_state,
		"seq" : seq,
		"run_id" : run_id
    }
    return record


def consumer_loop():
    pass
      
def producer_loop(args, stop_flag: dict, event_q: Queue, metrics: dict):
	run_id = create_run_id() 
	seq = 0

	sampler = PirSampler(args.pin)
	interp = PirInterpreter(cooldown_s=args.cooldown, min_high_s=args.min_high)

	while not stop_flag["stop"]:
		
		try:
			now = time.time()
			raw = sampler.read()
		except Exception as exc:
			print(f"[producer] sensor read error: {exc}", file=sys.stderr)
			continue

		for event in interp.update(raw, now):
			seq += 1
			event_time = epoch_to_utc_iso(event["t"])

			record = create_event(
					event_time = event_time,
					device_id = args.device_id,
					event_type = "motion",
					motion_state = "detected",
					seq = seq,
					run_id = run_id,
				)
			try:
				event_q.put_nowait(record)
				metrics["produced"] += 1

				if args.verbose:
					print(f"[producer] queued seq={seq} state={record['motion_state']} event_time={event_time}")


			except queue.Full:
				metrics["dropped"] += 1
				if args.verbose:
					print(f"[producer] queue full, dropped seq={seq}", file=sys.stderr)
		time.sleep(args.sample_interval)

		

def main() -> int:
	args = parse_args()
	validate_args(args)   
	
	written = 0
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
				f"cooldown={args.cooldown}s min_high={args.min_high}s duration={args.duration}s out={args.out}"
			)

		t_end = time.time() + args.duration
     #########################



	except KeyboardInterrupt:
		print(f"\n[logger] Ctrl-C: exit. records_written={written}")
		return 0
	except Exception as exc:
		print(f"[logger] runtime error: {exc}", file=sys.stderr)
		return 1

	print(f"[logger] done. run_id={run_id} records_written={written}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())