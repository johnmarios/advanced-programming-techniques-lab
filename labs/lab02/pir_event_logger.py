# import argparse
# import json
# import sys
# import time
# from datetime import datetime, timezone
# import uuid

# from pirlib.interpreter import PirInterpreter
# from pirlib.sampler import PirSampler

# def create_run_id() -> str:
#     '''generates a unique run ID using UUID4'''
#     run_id = str(uuid.uuid4())
#     return run_id

# def utc_now_iso() -> str:
# 	'''Get the current UTC time as an ISO 8601 string with milliseconds precision.'''
# 	return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


# def epoch_to_utc_iso(epoch_seconds: float) -> str:
# 	'''Convert epoch seconds to ISO 8601 UTC string with milliseconds precision.'''
# 	return datetime.fromtimestamp(epoch_seconds, tz=timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


# def parse_args() -> argparse.Namespace:
# 	parser = argparse.ArgumentParser(description="PIR event logger (JSONL)")
# 	parser.add_argument("--device-id", required=True)
# 	parser.add_argument("--pin", type=int, required=True)
# 	parser.add_argument("--sample-interval", type=float, default=0.1)
# 	parser.add_argument("--cooldown", type=float, default=0.0)
# 	parser.add_argument("--min-high", type=float, default=0.0)
# 	parser.add_argument("--duration", type=float, default=60.0)
# 	parser.add_argument("--out", required=True)
# 	parser.add_argument("--verbose", action="store_true")
# 	args = parser.parse_args()

# 	if args.pin < 0:
# 		parser.error("--pin must be >= 0")
# 	if args.sample_interval <= 0:
# 		parser.error("--sample-interval must be > 0")
# 	if args.cooldown < 0:
# 		parser.error("--cooldown must be >= 0")
# 	if args.min_high < 0:
# 		parser.error("--min-high must be >= 0")
# 	if args.duration <= 0:
# 		parser.error("--duration must be > 0")

# 	return args


# def main() -> int:
# 	args = parse_args()

# 	run_id = create_run_id()
# 	seq = 0
# 	written = 0

# 	try:
# 		sampler = PirSampler(args.pin)
# 		interp = PirInterpreter(cooldown_s=args.cooldown, min_high_s=args.min_high)

# 		if args.verbose:
# 			print(
# 				f"[logger] device={args.device_id} pin={args.pin} interval={args.sample_interval}s "
# 				f"cooldown={args.cooldown}s min_high={args.min_high}s duration={args.duration}s out={args.out}"
# 			)

# 		t_end = time.time() + args.duration

# 		with open(args.out, "a", encoding="utf-8") as fp:
# 			while time.time() < t_end:
# 				now = time.time()
# 				raw = sampler.read()

# 				for ev in interp.update(raw, now):
# 					seq += 1
# 					event_time = epoch_to_utc_iso(ev["t"])
# 					ingest_time = utc_now_iso()
# 					record = {
# 						"event_time": event_time,
# 						"ingest_time": ingest_time,
# 						"device_id": args.device_id,
# 						"event_type": "motion",
# 						"motion_state": "detected",
# 						"seq": seq,
# 						"run_id": run_id,
# 						"pin": args.pin,
# 						"sample_interval_s": args.sample_interval,
# 						"cooldown_s": args.cooldown,
# 						"min_high_s": args.min_high,
# 					}
# 					fp.write(json.dumps(record, ensure_ascii=False) + "\n")
# 					fp.flush()
# 					written += 1

# 					if args.verbose:
# 						print(f"[logger] seq={seq} event_time={event_time} ingest_time={ingest_time}")

# 				time.sleep(args.sample_interval)

# 	except KeyboardInterrupt:
# 		print(f"\n[logger] Ctrl-C: exit. records_written={written}")
# 		return 0
# 	except Exception as exc:
# 		print(f"[logger] runtime error: {exc}", file=sys.stderr)
# 		return 1

# 	print(f"[logger] done. run_id={run_id} records_written={written}")
# 	return 0


# if __name__ == "__main__":
# 	raise SystemExit(main())



###

import argparse
import json
import sys
import time
from datetime import datetime, timezone
import uuid

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


def main() -> int:
	args = parse_args()
	validate_args(args)
	run_id = create_run_id()    
	seq = 0
	written = 0

	try:
		sampler = PirSampler(args.pin)
		interp = PirInterpreter(cooldown_s=args.cooldown, min_high_s=args.min_high)

		if args.verbose:
			print(
				f"[logger] device={args.device_id} pin={args.pin} interval={args.sample_interval}s "
				f"cooldown={args.cooldown}s min_high={args.min_high}s duration={args.duration}s out={args.out}"
			)

		t_end = time.time() + args.duration

		with open(args.out, "a", encoding="utf-8") as fp:
			while time.time() < t_end:
				now = time.time()
				raw = sampler.read()

				for ev in interp.update(raw, now):
					seq += 1
					event_time = epoch_to_utc_iso(ev["t"])
					ingest_time = utc_now_iso()
					record = {
						"event_time": event_time,
						"ingest_time": ingest_time,
						"device_id": args.device_id,
						"event_type": "motion",
						"motion_state": "detected",
						"seq": seq,
						"run_id": run_id,
						"pin": args.pin,
						"sample_interval_s": args.sample_interval,
						"cooldown_s": args.cooldown,
						"min_high_s": args.min_high,
					}
					fp.write(json.dumps(record) + "\n")
					fp.flush()
					written += 1

					if args.verbose:
						print(f"[logger] seq={seq} event_time={event_time} ingest_time={ingest_time}")

				time.sleep(args.sample_interval)

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