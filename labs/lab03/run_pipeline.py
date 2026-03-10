from queue import Queue, Empty
import argparse
from datetime import datetime, timezone
import json
import time



def utc_now_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )
def parse_iso_utc(s: str):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

def jsonl_append_event(filename, event):
    with open(filename, "a", encoding="utf-8") as fp:
        json.dump(event, fp)
        fp.write("\n")

def metrics_init()->dict:
    metrics = {
        "produced": 0,
        "consumed": 0,
        "dropped": 0,
        "max_queue": 0,
    }
    return metrics


stop_flag = {"stop": False}

def parse_args():
    p = argparse.ArgumentParser(description="PIR event pipeline")
    p.add_argument("--device-id", required=True)
    p.add_argument("--pin", type=int, required=True)
    p.add_argument("--sample-interval", type=float, default=0.1)
    p.add_argument("--cooldown", type=float, default=0.0)
    p.add_argument("--min-high", type=float, default=0.0)
    p.add_argument("--duration", type=float, default=60.0)
    p.add_argument("--queue-size", type=int, default=10)
    p.add_argument("--out", required=True)
    return p.parse_args()


def validate_args(args):
    pass

def add_metrics(event, metrics):
    metrics["produced"] += 1
    if event["kind"] == "motion":
        metrics["consumed"] += 1


def producer():
    pass

def consumer():
    pass

def main():
    args = parse_args()
    validate_args(args)
    metrics=metrics_init()
    event_q = Queue(maxsize=args.queue_size)

if __name__ == "__main__":  
    main()