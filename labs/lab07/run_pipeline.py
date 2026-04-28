# import argparse
# import json
# import os
# import subprocess
# import sys
# import time
# from datetime import datetime, timezone
# import uuid
# from pathlib import Path

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

# 	''' Parse command-line arguments using argparse and return the parsed arguments as a Namespace object.'''

# 	parser = argparse.ArgumentParser(description="PIR event logger (JSONL)")
# 	parser.add_argument("--role", choices=["launch", "producer", "consumer"], default="launch")
# 	# launch 
# 	parser.add_argument("--consumers", type=int, default=1)
# 	parser.add_argument("--consumer-out-template", default="")
# 	parser.add_argument("--context", default="models/context.jsonld")
# 	parser.add_argument("--device-id")
# 	parser.add_argument("--wastebin-id", default="urn:dev:team-06:wastebin-01")
# 	parser.add_argument("--environment-id", default="urn:dev:team-06:environment-01")
# 	parser.add_argument("--broker", default="localhost")
# 	parser.add_argument("--port", type=int, default=1883)
# 	parser.add_argument("--topic", default="pir")
# 	parser.add_argument("--qos", type=int, default=0, choices=[0, 1, 2])
# 	parser.add_argument("--pin", type=int)
# 	parser.add_argument("--sample-interval", type=float, default=0.1)
# 	parser.add_argument("--cooldown", type=float, default=0.0)
# 	parser.add_argument("--min-high", type=float, default=0.0)
# 	parser.add_argument("--duration", type=float, default=60.0)
# 	parser.add_argument("--out")
# 	parser.add_argument("--consumer-delay", type=float, default=0.0)
# 	parser.add_argument("--verbose", action="store_true")
	
# 	return parser.parse_args()

# def validate_args(args):
# 	'''Validate the parsed command-line arguments and exit with an error message if any validation fails.'''
# 	# exit code 2 for invalid command-line arguments, exit code 1 for runtime errors (e.g. file I/O errors)
# 	if args.pin < 0:
# 		raise ValueError("--pin must be >= 0")
# 	if args.sample_interval <= 0:
# 		raise ValueError("--sample-interval must be > 0")
# 	if args.cooldown < 0:
# 		raise ValueError("--cooldown must be >= 0")
# 	if args.min_high < 0:
# 		raise ValueError("--min-high must be >= 0")
# 	if args.duration <= 0:
# 		raise ValueError("--duration must be > 0")
# 	if args.port <= 0 or args.port > 65535:
# 		raise ValueError("--port must be in range [1, 65535]")
# 	if args.consumer_delay < 0:
# 		raise ValueError("--consumer-delay must be >= 0")
# 	if args.consumers < 1:
# 		raise ValueError("--consumers must be >= 1")
# 	if args.role in ("producer", "launch"):
# 		if args.device_id is None:
# 			raise ValueError("--device-id is required for producer/launch role")
# 		if args.pin is None:
# 			raise ValueError("--pin is required for producer/launch role")
# 	if args.role in ("consumer", "launch"):
# 		if not args.out:
# 			raise ValueError("--out is required for consumer/launch role")
# 	if args.consumer_out_template and "{i}" not in args.consumer_out_template:
# 		raise ValueError("--consumer-out-template must contain '{i}' placeholder")
    

# def append_jsonl_newline(path: Path) -> None:
#     with path.open("a", encoding="utf-8") as f:
#         f.write("\n")

# def append_jsonl_line(path: Path, record: dict) -> None:
#     # One JSON object per line, append-only
#     with path.open("a", encoding="utf-8") as f:
#         f.write(json.dumps(record) + "\n")

# def normalize_entity_id(value: str, default_prefix: str = "urn:dev:team-06:") -> str:
# 	if value.startswith("urn:"):
# 		return value
# 	return f"{default_prefix}{value}"


# def create_event(
# 	event_time: str,
# 	device_id: str,
# 	wastebin_id: str,
# 	environment_id: str,
# 	event_type: str,
# 	seq: int,
# 	run_id: str,
# 	motion_state: str,
# 	context_iri: str,
# ) -> dict:
#     '''Create a single event record dictionary based on the provided parameters.'''
#     record = {
# 		"@context": context_iri,
# 		"@type": "sosa:Observation",
#         "event_time" : event_time,
# 		"device_id" : normalize_entity_id(device_id),
# 		"wastebin_id" : normalize_entity_id(wastebin_id),
# 		"environment_id" : normalize_entity_id(environment_id),
# 		"event_type" : event_type,
# 		"motion_state" : motion_state,
# 		"seq" : seq,
# 		"run_id" : run_id
#     }
#     return record

# def setup():
# 	args = parse_args()
# 	validate_args(args)
# 	return args



