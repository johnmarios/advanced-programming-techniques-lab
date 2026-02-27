#!/usr/bin/env python3
"""
Smart Wastebin Mock Event Generator
-------------------------------------
Appends high-level wastebin events to a JSON Lines log file.

Usage:
    python event_generator.py \
        --device-id wastebin-01 \
        --event-type deposit \
        --count 10 \
        --interval 2 \
        --out events.log
"""

import argparse
import json
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def utc_now_iso() -> str:
    """Return current UTC time as an ISO-8601 string with millisecond precision.

    Example: 2026-02-10T12:34:56.789Z
    """
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )


def build_record(event_type: str, device_id: str, seq: int, deposit_total: int) -> dict:
    """Build a single event record."""
    record = {
        "seq":        seq,
        "event_id":   str(uuid.uuid4()),
        "event_type": event_type,
        "device_id":  device_id,
        "timestamp":  utc_now_iso(),
    }

    if event_type == "deposit":
        record["deposit_delta"] = 1
        record["deposit_total"] = deposit_total

    return record


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Emit mock wastebin events to a JSON Lines log file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "--device-id",
        required=True,
        metavar="ID",
        help="Identifier of the mock wastebin device (e.g. wastebin-01)",
    )
    parser.add_argument(
        "--event-type",
        required=True,
        choices=["deposit", "heartbeat"],
        metavar="TYPE",
        help="Type of event to emit: deposit | heartbeat",
    )
    parser.add_argument(
        "--count",
        required=True,
        type=int,
        metavar="N",
        help="Number of records to emit (must be > 0)",
    )
    parser.add_argument(
        "--interval",
        required=True,
        type=float,
        metavar="SECONDS",
        help="Seconds between emissions (must be >= 0)",
    )
    parser.add_argument(
        "--out",
        required=True,
        metavar="PATH",
        help="Output file path (opened in append mode)",
    )

    return parser.parse_args()


def validate(args: argparse.Namespace) -> None:
    """Validate argument values; print a clear message and exit on failure."""
    errors = []

    if not args.device_id.strip():
        errors.append("--device-id must not be empty")

    if args.count <= 0:
        errors.append("--count must be > 0")

    if args.interval < 0:
        errors.append("--interval must be >= 0")

    out_path = Path(args.out)
    if out_path.exists() and not out_path.is_file():
        errors.append(f"--out '{args.out}' exists but is not a regular file")

    if errors:
        for msg in errors:
            print(f"Error: {msg}", file=sys.stderr)
        raise SystemExit(2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    args = parse_args()
    validate(args)

    out_path   = Path(args.out)
    event_type = args.event_type
    device_id  = args.device_id
    count      = args.count
    interval   = args.interval

    # For deposit events we maintain a running total across this run.
    # We initialise it by counting existing deposit records in the log so that
    # the total is consistent even when the tool is called multiple times.
    deposit_total = 0
    if event_type == "deposit" and out_path.exists():
        try:
            with open(out_path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                        if rec.get("event_type") == "deposit":
                            deposit_total = max(
                                deposit_total,
                                rec.get("deposit_total", deposit_total),
                            )
                    except json.JSONDecodeError:
                        pass  # skip malformed lines silently
        except OSError:
            pass  # file not yet readable; start from 0

    written = 0
    print(
        f"[{utc_now_iso()}] Starting: device={device_id} "
        f"type={event_type} count={count} interval={interval}s out={out_path}"
    )

    try:
        with open(out_path, "a", encoding="utf-8") as f:
            for seq in range(1, count + 1):
                if event_type == "deposit":
                    deposit_total += 1

                record = build_record(event_type, device_id, seq, deposit_total)

                f.write(json.dumps(record) + "\n")
                f.flush()   # ensure each record hits the file immediately
                written += 1

                print(
                    f"  [{record['timestamp']}] seq={seq:>4}  "
                    f"type={event_type}"
                    + (f"  total={deposit_total}" if event_type == "deposit" else "")
                )

                # Sleep between records, but not after the last one
                if interval > 0 and seq < count:
                    time.sleep(interval)

    except KeyboardInterrupt:
        print(f"\n[interrupted] Wrote {written} of {count} record(s) to '{out_path}'.")
        raise SystemExit(130)  # standard exit code for SIGINT

    except OSError as exc:
        print(f"Error writing to '{out_path}': {exc}", file=sys.stderr)
        raise SystemExit(1)

    print(f"[{utc_now_iso()}] Done. Wrote {written} record(s) to '{out_path}'.")


if __name__ == "__main__":
    main()
