import argparse
import json
import sys
import time
from collections import deque
from pathlib import Path

import paho.mqtt.client as mqtt


def append_jsonl_newline(path: Path) -> None:
	with path.open("a", encoding="utf-8") as f:
		f.write("\n")

def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Storage/Logger consumer")
	parser.add_argument("--broker", default="localhost") # MQTT broker address (default: localhost)
	parser.add_argument("--port", type=int, default=1883)
	parser.add_argument("--topic", default="pir")
	parser.add_argument("--qos", type=int, default=0, choices=[0, 1, 2])
	parser.add_argument("--out", required=True)
	parser.add_argument("--cache-size", type=int, default=100)
	parser.add_argument("--consumer-delay", type=float, default=0.0) # Delay between processing messages (seconds)
	parser.add_argument("--duration", type=float, default=60.0) # Total duration to run the consumer (seconds, >0), or 0 for infinite
	parser.add_argument("--verbose", action="store_true")
	return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
	if args.duration <= 0:
		raise ValueError("--duration must be > 0")
	if args.port <= 0 or args.port > 65535:
		raise ValueError("--port must be in range [1, 65535]")
	if args.consumer_delay < 0:
		raise ValueError("--consumer-delay must be >= 0")
	if args.cache_size < 1:
		raise ValueError("--cache-size must be >= 1")


class Consumer:
	'''MQTT consumer that subscribes to a topic and appends received messages to a JSONL file.'''
	static_counter = 0 # static counter to generate unique MQTT client IDs for multiple consumer instances

	def __init__(self, args, metrics, stop_flag):
		self.args = args
		self.metrics = metrics
		self.stop_flag = stop_flag # shared flag to signal the consumer to stop consuming messages
		self.out_path = Path(args.out)
		self.out_file = None
		self.seen_message_keys = set() # keys : run_id:seq or canonical JSON string of the record
		self.seen_message_order = deque() # to track the order of seen message keys for eviction from the cache when it exceeds the specified size

		client_id = f"C{Consumer.static_counter}"
		Consumer.static_counter += 1
		self.client = mqtt.Client(client_id=client_id)
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message

	def get_record_key(self, record: dict) -> str:
		''' generates a unique key string for a given event record dictionary, which is used for duplicate detection; '''
		run_id = record.get("run_id") 
		seq = record.get("seq")
		if run_id is not None and seq is not None:
			return f"{run_id}:{seq}"
		return json.dumps(record, sort_keys=True, separators=(",", ":"))

	def is_duplicate(self, record: dict) -> bool:
		key = self.get_record_key(record)
		if key in self.seen_message_keys:
			return True

		# if it's not a duplicate
		self.seen_message_keys.add(key)
		self.seen_message_order.append(key)

		# handle the case where the cache exceeds the specified size
		# by evicting the oldest seen message key from the cache to prevent unbounded memory growth
		while len(self.seen_message_order) > self.args.cache_size: 
			old_key = self.seen_message_order.popleft() 
			self.seen_message_keys.discard(old_key)

		return False

	def on_connect(self, client, reason_code, properties=None):
		if reason_code == 0: # successful connection
			client.subscribe(self.args.topic, qos=self.args.qos)
			if self.args.verbose:
				print(f"[consumer] subscribed topic={self.args.topic}", flush=True)
		else:
			print(f"[consumer] connect failed rc={reason_code}", file=sys.stderr, flush=True)

	def on_message(self, msg):
		try:
			# decode the MQTT message payload from bytes to string and parse it as JSON to get the event record dictionary
			record = json.loads(msg.payload.decode("utf-8"))

			# Drop duplicate events using bounded in-memory cache.
			if self.is_duplicate(record):
				self.metrics["dropped"] += 1
				if self.args.verbose:
					print(
						f"[consumer] duplicate record detected, dropping run_id={record.get('run_id')} seq={record.get('seq')}",
						flush=True,
					)
				return
			# writes the event record as a JSON line to the output file and flushes it to ensure it's written to disk
			self.out_file.write(json.dumps(record) + "\n")
			self.out_file.flush()
			self.metrics["consumed"] += 1

			if self.args.verbose:
				print(
					f"[consumer-storage] wrote seq={record.get('seq')} bin={record.get('wastebin_id')}",
					flush=True,
				)

			if self.args.consumer_delay > 0:
				time.sleep(self.args.consumer_delay)
		except Exception as exc:
			print(f"[consumer] message handling error: {exc}", file=sys.stderr, flush=True)

	def consume(self):
		self.out_file = self.out_path.open("a", encoding="utf-8")
		try:
			self.client.connect(self.args.broker, self.args.port, 60)
			self.client.loop_start()
			start_t = time.time()
			while not self.stop_flag["stop"]:
				if self.args.duration > 0 and (time.time() - start_t) >= self.args.duration:
					break
				# time.sleep(0.2) 
		finally:
			self.client.loop_stop()
			self.client.disconnect() # ensure MQTT client is properly disconnected
			self.out_file.close()
			append_jsonl_newline(self.out_path)


def main() -> int:
	try:
		args = parse_args()
		validate_args(args)
	except Exception as exc:
		print(f"[consumer-storage] argument error: {exc}", file=sys.stderr)
		return 2

	metrics = {"produced": 0, "consumed": 0, "dropped": 0}
	stop_flag = {"stop": False} 

	try:
		consumer = Consumer(args=args, metrics=metrics, stop_flag=stop_flag)

		if args.verbose:
			print(
				f"[consumer-storage] broker={args.broker}:{args.port} topic={args.topic} qos={args.qos} "
				f"duration={args.duration}s out={args.out} delay={args.consumer_delay}s cache={args.cache_size}",
				flush=True,
			)

		try:
			consumer.consume()
		except KeyboardInterrupt:
			print("\n[consumer-storage] Ctrl-C: stopping...", flush=True)
			stop_flag["stop"] = True # signal the consumer to stop consuming messages

	except Exception as exc:
		print(f"[consumer-storage] runtime error: {exc}", file=sys.stderr)
		return 1

	print(f"[consumer-storage] done. consumed={metrics['consumed']}", flush=True)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
