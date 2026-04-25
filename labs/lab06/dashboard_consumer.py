import argparse
import json
import sys
import time

import paho.mqtt.client as mqtt


class DashboardConsumer:
    static_counter = 0

    def __init__(self, args):
        self.args = args

        client_id = f"D{DashboardConsumer.static_counter}"
        DashboardConsumer.static_counter += 1
        self.client = mqtt.Client(client_id=client_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message

    def _on_connect(self, client, userdata, flags, reason_code, properties=None):
        if reason_code == 0:
            client.subscribe(self.args.topic, qos=self.args.qos)
            print(f"[consumer-dashboard] subscribed topic={self.args.topic}", flush=True)
        else:
            print(f"[consumer-dashboard] connect failed rc={reason_code}", file=sys.stderr, flush=True)

    def _on_message(self, client, userdata, msg):
        try:
            record = json.loads(msg.payload.decode("utf-8"))
            print(
                "[dashboard] "
                f"t={record.get('event_time')} "
                f"seq={record.get('seq')} "
                f"bin={record.get('wastebin_id')} "
                f"state={record.get('motion_state')}",
                flush=True,
            )

            if self.args.consumer_delay > 0:
                time.sleep(self.args.consumer_delay)

        except Exception as exc:
            print(f"[consumer-dashboard] message handling error: {exc}", file=sys.stderr, flush=True)

    def run(self):
        self.client.connect(self.args.broker, self.args.port, 60)
        self.client.loop_start()
        try:
            start_t = time.time()
            while True:
                if self.args.duration > 0 and (time.time() - start_t) >= self.args.duration:
                    break
                time.sleep(0.2)
        finally:
            self.client.loop_stop()
            self.client.disconnect()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dashboard consumer")
    parser.add_argument("--broker", default="localhost")
    parser.add_argument("--port", type=int, default=1883)
    parser.add_argument("--topic", default="pir")
    parser.add_argument("--qos", type=int, default=0, choices=[0, 1, 2])
    parser.add_argument("--consumer-delay", type=float, default=0.0)
    parser.add_argument("--duration", type=float, default=60.0)
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    if args.duration <= 0:
        raise ValueError("--duration must be > 0")
    if args.port <= 0 or args.port > 65535:
        raise ValueError("--port must be in range [1, 65535]")
    if args.consumer_delay < 0:
        raise ValueError("--consumer-delay must be >= 0")


def main() -> int:
    try:
        args = parse_args()
        validate_args(args)
    except Exception as exc:
        print(f"[consumer-dashboard] argument error: {exc}", file=sys.stderr)
        return 2

    try:
        consumer = DashboardConsumer(args)
        try:
            consumer.run()
        except KeyboardInterrupt:
            print("\n[consumer-dashboard] Ctrl-C: stopping...", flush=True)

    except Exception as exc:
        print(f"[consumer-dashboard] runtime error: {exc}", file=sys.stderr)
        return 1

    print("[consumer-dashboard] done.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
