import json
from datetime import datetime, timezone
import sys
import uuid
import argparse
import time
from pathlib import Path
    
lid_open = False
maintenance = False

def apply_state_transition(event_type: str) -> None:
    '''Update the global state variables based on the event type.'''
    global lid_open, maintenance
    
    if event_type == "lid_open":
        lid_open = True
    elif event_type == "lid_close":
        lid_open = False
    elif event_type == "maintenance":
        maintenance = True
    elif event_type == "maintenance_termination":
        maintenance = False

def utc_now_iso() -> str:
    '''creates a UTC timestamp in ISO 8601 format with milliseconds precision'''
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

def append_jsonl_newline(path: Path) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write("\n")

def append_jsonl_line(path: Path, record: dict) -> None:
    # One JSON object per line, append-only
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

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

    parser.add_argument("--starting-total", type=int, default=None)
    parser.add_argument("--deposit-delta", type=int, default=1)
    parser.add_argument("--verbose", action="store_true") # if verbose appears in command-line, will be set to True, otherwise it will be False
    # store_true means that if the flag is present, it will set the value to True, and if it's absent, it will set the value to False
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

    if args.deposit_delta <= 0:
        print("Error: --deposit-delta must be > 0", file=sys.stderr)
        raise SystemExit(2)

    if args.event_type not in {"deposit", "heartbeat", "lid_open", "lid_close", "lid_clear", "maintenance", "maintenance_termination"}:
        print("Error: --event-type must be 'deposit', 'heartbeat', 'lid_open', 'lid_close', 'lid_clear', 'maintenance', or 'maintenance_termination'", file=sys.stderr)
        raise SystemExit(2)

def load_previous_state(path: Path) -> None:
    '''Restore state by scanning from the bottom and applying the latest state transition.'''
    # updates the global state variables

    global lid_open, maintenance

    if not path.exists():
        return

    with path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    lid_state_found = False
    maintenance_state_found = False

    for line in reversed(lines):
        if line.strip() == "":
            continue
        record = json.loads(line)
        event_type = record.get("event_type")

        if not lid_state_found and event_type == "lid_open":
            lid_open = True
            lid_state_found = True
        elif not lid_state_found and event_type == "lid_close":
            lid_open = False
            lid_state_found = True

        if not maintenance_state_found and event_type == "maintenance":
            maintenance = True
            maintenance_state_found = True
        elif not maintenance_state_found and event_type == "maintenance_termination":
            maintenance = False
            maintenance_state_found = True

        if lid_state_found and maintenance_state_found:
            break


def get_last_record(path: Path) -> dict | None:
    '''get the last record from the JSONL file, return None if file does not exist or is empty'''
    if not path.exists():
        return None

    last_record = None
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip() == "": # skip empty lines
                continue
            last_record = json.loads(line) # parse the JSON string into a Python dictionary

    return last_record

def get_deposit_total(path: Path) -> int | None:
    '''Return the latest deposit_total found in the log, otherwise None.'''
    if not path.exists():
        return None

    with path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in reversed(lines):
        if line.strip() == "":
            continue
        record = json.loads(line)
        value = record.get("deposit_total")
        if isinstance(value, int):
            return value

    return None

def create_event(event_time: str, ingest_time: str, device_id: str, event_type: str, seq: int, run_id: str, deposit_total: int, deposit_delta: int = 1, starting_total: int = 0) -> dict:
    '''Create a single event record dictionary based on the provided parameters.'''
    record = {
        "event_time": event_time,
        "ingest_time": ingest_time,
        "device_id": device_id,
        "event_type": event_type,
        "seq": seq,
        "run_id": run_id,
    }

    if event_type == "deposit" and maintenance:
        record["deposit_delta"] = 0
        record["deposit_total"] = deposit_total
        if starting_total is not None: record["starting_total"] = starting_total 
        record["status"] = "rejected"
        record["reason"] = "maintenance_mode"

    elif event_type == "deposit" and lid_open:
        record["deposit_delta"] = deposit_delta
        record["deposit_total"] = deposit_total
        if starting_total is not None: record["starting_total"] = starting_total 
        record["status"] = "accepted"
    
    elif event_type == "deposit" and not lid_open:
        record["deposit_delta"] = 0 
        record["deposit_total"] = deposit_total
        if starting_total is not None: record["starting_total"] = starting_total 
        record["status"] = "rejected"
        record["reason"] = "lid_closed"

    elif event_type == "heartbeat":
        record["status"] = "online"

    elif event_type == "lid_clear":
        record["action"] = "cleared"
        record["deposit_total"] = deposit_total


    return record

def configure_deposit_total(starting_total: int | None, out_path: Path) -> int:
    last_deposit_total = get_deposit_total(out_path) # gets the latest deposit total from the log
    # if starting total is provided in CLI (even 0), always use it
    if starting_total is not None:
        return starting_total
    # if starting total is omitted, continue from previous total when available
    if last_deposit_total is not None:
        return last_deposit_total
    return 0

def main():
    # parse and validate command-line arguments
    args = parse_args()
    validate_args(args)

    out_path = Path(args.out) # convert the output file path string to a Path object for easier file handling
    
    # the global state variables are updated based on previous state and current event 
    load_previous_state(out_path)
    apply_state_transition(args.event_type) 
    
    # deposit_total is either the last deposit total from the previous state (if exists) and starting-total isn't provided,
    # or the starting total provided in the command-line arguments 
    deposit_total = configure_deposit_total(args.starting_total, out_path)
    
    run_id = create_run_id()
    written = 0 # counter for number of records successfully written to the output file 

    try:
        # taking count into consideration
        for seq in range(1, args.count + 1): 
            # timestamps are generated 
            event_time = utc_now_iso()
            ingest_time = utc_now_iso()

            if args.event_type == "deposit" and lid_open and not maintenance:
                deposit_total += args.deposit_delta
            elif args.event_type == "lid_clear":
                deposit_total = 0

            record = create_event(
                event_time=event_time,
                ingest_time=ingest_time,
                device_id=args.device_id,
                event_type=args.event_type,
                seq=seq,
                run_id=run_id,
                deposit_total=deposit_total,
                deposit_delta=args.deposit_delta,
                starting_total=args.starting_total
            )

            append_jsonl_line(out_path, record)
        
            written += 1

            # if verbose flag exists, then it's set and it prints message every 5 records
            if args.verbose and (seq % 5 == 0):
                print(f"generated seq={seq} type={args.event_type} out={out_path}")

            if args.interval > 0 and seq < args.count:
                time.sleep(args.interval)

        print(f"Done. Wrote {written} record(s).")
        append_jsonl_newline(out_path) # for better formatting 

    except KeyboardInterrupt:
        # handling Ctrl-C
        print(f"\nInterrupted. Wrote {written} record(s).", file=sys.stderr)
        raise SystemExit(0)

    except OSError as e:
        print(f"Runtime error (I/O): {e}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
