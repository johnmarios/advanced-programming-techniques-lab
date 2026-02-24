#!/usr/bin/env python3
import argparse
import json
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path


def utc_now_iso() -> str:
    # Example: 2026-02-10T12:34:56.789Z
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Mock wastebin event generator (JSON Lines append-only log)."
    )
    p.add_argument("--device-id", required=True, type=str, help="Device identifier (string).")
    p.add_argument(
        "--event-type",
        required=True,
        type=str,
        help="Event type: deposit or heartbeat.",
    )
    p.add_argument("--count", required=True, type=int, help="Number of records to emit (>0).")
    p.add_argument(
        "--interval",
        required=True,
        type=float,
        help="Seconds between emissions (>=0).",
    )
    p.add_argument(
        "--out",
        required=True,
        type=str,
        help="Output file path (append mode).",
    )
    p.add_argument(
        "--starting-total",
        type=int,
        default=0,
        help="Initial deposit total (default 0). Used only for deposit events.",
    )
    p.add_argument(
        "--verbose",
        action="store_true",
        help="Print operational progress to stderr every 5 records.",
    )
    return p.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    if args.count <= 0:
        print("Error: --count must be > 0", file=sys.stderr)
        raise SystemExit(2)

    if args.interval < 0:
        print("Error: --interval must be >= 0", file=sys.stderr)
        raise SystemExit(2)

    if args.event_type not in {"deposit", "heartbeat"}:
        print("Error: --event-type must be 'deposit' or 'heartbeat'", file=sys.stderr)
        raise SystemExit(2)

    # starting-total: allow any int, but it only makes sense for deposit
    # (we keep it permissive; consumers can still ignore it for heartbeat)


def append_jsonl_line(path: Path, record: dict) -> None:
    # One JSON object per line, append-only
    line = json.dumps(record, ensure_ascii=False)
    with path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")
        f.flush()


def main() -> None:
    args = parse_args()
    validate_args(args)

    out_path = Path(args.out)
    run_id = str(uuid.uuid4())

    deposit_total = args.starting_total
    written = 0

    try:
        for seq in range(1, args.count + 1):
            event_time = utc_now_iso()
            ingest_time = utc_now_iso()

            record = {
                "event_time": event_time,
                "ingest_time": ingest_time,
                "device_id": args.device_id,
                "event_type": args.event_type,
                "seq": seq,
                "run_id": run_id,
            }

            if args.event_type == "deposit":
                deposit_total += 1
                record["deposit_delta"] = 1
                record["deposit_total"] = deposit_total
            else:  # heartbeat
                record["status"] = "online"

            append_jsonl_line(out_path, record)
            written += 1

            # operational log (human-readable) -> stderr, never to JSONL file
            if args.verbose and (seq % 5 == 0):
                print(
                    f"generated seq={seq} type={args.event_type} out={out_path}",
                    file=sys.stderr,
                )

            if args.interval > 0 and seq < args.count:
                time.sleep(args.interval)

        print(f"Done. Wrote {written} record(s). run_id={run_id}", file=sys.stderr)

    except KeyboardInterrupt:
        print(f"\nInterrupted. Wrote {written} record(s). run_id={run_id}", file=sys.stderr)
        # exit 0 is fine on Ctrl-C; spec only asks graceful shutdown
        raise SystemExit(0)

    except OSError as e:
        print(f"Runtime error (I/O): {e}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()