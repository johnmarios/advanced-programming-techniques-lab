import json
from datetime import datetime, timezone
import sys
import uuid
import argparse
import time
    

def utc_now_iso() -> str:
    '''creates a UTC timestamp in ISO 8601 format with milliseconds precision'''
    # Example: 2026-02-10T12:34:56.789Z
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )
def ingest_time_iso() -> str:
    '''creates a UTC timestamp in ISO 8601 format with milliseconds precision for ingest_time field'''
    # Example: 2026-02-10T12:34:56.789Z
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )

def create_run_id() -> str:
    '''generates a unique run ID using UUID4'''
    run_id = str(uuid.uuid4())
    return run_id

def create_event(event_time: str, ingest_time: str, device_id: str, event_type: str, seq: int, run_id: str, deposit_total: int, deposit_delta: int = 1, starting_total: int = 0) -> dict:
    """Create a single event record dictionary."""

    event = {
        "event_time": event_time,
        "ingest_time": ingest_time,
        "device_id": device_id,
        "event_type": event_type,
        "seq": seq,
        "run_id": run_id,

    }

    if event_type == "deposit":
        event["deposit_delta"] = deposit_delta
        event["deposit_total"] = deposit_total
        event["starting_total"] = starting_total

    elif event_type == "heartbeat":
        event["status"] = "online"

    return event


def parse_args():
    '''Parse command-line arguments using argparse.'''
    # create an ArgumentParser object to define expected command-line arguments and options
    parser = argparse.ArgumentParser(description="Mock wastebin event generator") # description shown in --help

    # required arguments for generating events
    parser.add_argument("--device-id", required=True)
    parser.add_argument("--event-type", required=True)
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--interval", type=float, required=True)
    parser.add_argument("--out", required=True)

    parser.add_argument("--starting-total", type=int, default=0)
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args() # parse the command-line arguments and return them as a Namespace object

def validate_args(args):
    '''Validate the parsed command-line arguments and exit with an error message if any validation fails.'''
    # exit code 2 for invalid command-line arguments, exit code 1 for runtime errors (e.g. file I/O errors)
    if args.count <= 0:
        print("Error: --count must be > 0", file=sys.stderr)
        # number of args : 7
        raise SystemExit(2) # exit with status code 2 to indicate invalid command-line arguments

    if args.interval < 0: # interval can be 0 for no delay, but cannot be negative
        print("Error: --interval must be >= 0", file=sys.stderr)
        raise SystemExit(2)

    if args.event_type not in {"deposit", "heartbeat"}:
        print("Error: --event-type must be 'deposit' or 'heartbeat'", file=sys.stderr)
        raise SystemExit(2)

def main():
    # parse and validate command-line arguments
    args = parse_args()
    validate_args(args)

    run_id = create_run_id()
    deposit_total = args.starting_total
    written = 0 # counter for number of records successfully written to the output file 
    event_time = utc_now_iso() # generate event_time once at the start of the run, all events in this run will have the same event_time

    try:
        # args.out is the output file path specified by the user, open it in append mode ("a") to add new events without overwriting existing content
        with open(args.out, "a", encoding="utf-8") as f:

            for seq in range(1, args.count + 1):

                if args.event_type == "deposit":
                    deposit_total += 1
                    record = create_event(
                        device_id=args.device_id,
                        event_type="deposit",
                        ingest_time=ingest_time_iso(),
                        seq=seq,
                        run_id=run_id,          
                        deposit_total=deposit_total,
                        event_time=event_time,
                    )
                else:
                    record = create_event(
                        device_id=args.device_id,
                        event_type="heartbeat",
                        ingest_time=ingest_time_iso(),
                        seq=seq,
                        run_id=run_id,
                        count = args.count,    
                        event_time=event_time,       
                    )

                f.write(json.dumps(record) + "\n")
                f.flush()

                written += 1

                if args.verbose and seq % 5 == 0:
                    print(
                        f"generated seq={seq} "
                        f"type={args.event_type} "
                        f"out={args.out} "
                    )

                if args.interval > 0:
                    time.sleep(args.interval)

    except KeyboardInterrupt:
        print(f"\nInterrupted. Wrote {written} record(s).")

    except OSError as e:
        print(f"Runtime error: {e}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
