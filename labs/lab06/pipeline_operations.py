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

def setup():
	args = parse_args()
	validate_args(args)
	event_q = Queue(maxsize=args.queue_size) # in-memory queue for events
	metrics = {"produced": 0, "dropped": 0, "max_queue": 0} # simple metrics tracking
	return args, event_q, metrics


		
