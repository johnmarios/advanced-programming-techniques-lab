import argparse
import json
import threading
import time
import uuid
from datetime import datetime, timezone
from queue import Empty, Full, Queue

from pirlib.sampler import PirSampler
from pirlib.interpreter import PirInterpreter


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def utc_now_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )


def parse_iso_utc(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="PIR event pipeline")
    p.add_argument("--device-id",       required=True)
    p.add_argument("--pin",             type=int,   required=True)
    p.add_argument("--sample-interval", type=float, default=0.1)
    p.add_argument("--cooldown",        type=float, default=0.0)
    p.add_argument("--min-high",        type=float, default=0.0)
    p.add_argument("--queue-size",      type=int,   default=100)
    p.add_argument("--consumer-delay",  type=float, default=0.0)
    p.add_argument("--duration",        type=float, default=60.0)
    p.add_argument("--out",             required=True)
    p.add_argument("--verbose",         action="store_true", default=False)
    return p.parse_args()


def validate_args(args):
    if args.sample_interval <= 0:
        raise ValueError("--sample-interval must be positive")
    if args.duration <= 0:
        raise ValueError("--duration must be positive")
    if args.queue_size < 1:
        raise ValueError("--queue-size must be at least 1")


# ---------------------------------------------------------------------------
# Producer
# ---------------------------------------------------------------------------

def producer_loop(event_q, sampler, interp, args, metrics, stop_flag):
    run_id = str(uuid.uuid4())
    seq = 0

    while not stop_flag["stop"]:
        current_time = time.monotonic()
        sample = sampler.read()

        for event in interp.update(sample, current_time):
            seq += 1

            record = {
                "event_time":   utc_now_iso(),
                "device_id":    args.device_id,
                "event_type":   "motion",
                "motion_state": "detected",
                "seq":          seq,
                "run_id":       run_id,
            }

            try:
                event_q.put_nowait(record)
                metrics["produced"] += 1
            except Full:
                metrics["dropped"] += 1

        time.sleep(args.sample_interval)


# ---------------------------------------------------------------------------
# Consumer
# ---------------------------------------------------------------------------

def consumer_loop(event_q, output_path, args, metrics, stop_flag):
    with open(output_path, "a", encoding="utf-8") as f:
        while not stop_flag["stop"] or not event_q.empty():
            try:
                record = event_q.get(timeout=0.5)
            except Empty:
                continue

            record["ingest_time"] = utc_now_iso()
            record["pipeline_latency_ms"] = (
                parse_iso_utc(record["ingest_time"]) - parse_iso_utc(record["event_time"])
            ).total_seconds() * 1000

            f.write(json.dumps(record) + "\n")
            f.flush()

            metrics["consumed"] += 1
            metrics["max_queue"] = max(metrics["max_queue"], event_q.qsize())

            event_q.task_done()

            if args.consumer_delay:
                time.sleep(args.consumer_delay)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    validate_args(args)

    metrics = {
        "produced": 0,
        "consumed": 0,
        "dropped":  0,
        "max_queue": 0,
    }
    stop_flag = {"stop": False}
    event_q   = Queue(maxsize=args.queue_size)

    sampler = PirSampler(pin=args.pin)
    interp  = PirInterpreter(cooldown=args.cooldown, min_high=args.min_high)

    producer_t = threading.Thread(
        target=producer_loop,
        args=(event_q, sampler, interp, args, metrics, stop_flag),
        daemon=True,
    )
    consumer_t = threading.Thread(
        target=consumer_loop,
        args=(event_q, args.out, args, metrics, stop_flag),
        daemon=True,
    )

    producer_t.start()
    consumer_t.start()
    print(f"[main] pipeline started  (duration={args.duration}s, out={args.out})")

    start_t = time.time()

    try:
        while (time.time() - start_t) < args.duration:
            if args.verbose:
                print(
                    f"[status] produced={metrics['produced']} "
                    f"consumed={metrics['consumed']} "
                    f"dropped={metrics['dropped']} "
                    f"queue={event_q.qsize()} "
                    f"max_queue={metrics['max_queue']}"
                )
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\n[main] Ctrl-C: stopping...")
    finally:
        stop_flag["stop"] = True
        producer_t.join()
        event_q.join()   # drain every item the producer enqueued
        consumer_t.join()

        print("[main] shutdown complete")
        print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()