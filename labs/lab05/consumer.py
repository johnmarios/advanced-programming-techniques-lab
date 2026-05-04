import json
import sys
import time
from datetime import datetime
from pathlib import Path

import paho.mqtt.client as mqtt

from labs.lab06.run_pipeline import append_jsonl_newline, utc_now_iso


class Consumer:
	static_counter = 0

	def __init__(self, args, metrics, stop_flag):
		self.args = args
		self.metrics = metrics
		self.stop_flag = stop_flag
		self.out_path = Path(args.out)
		self.out_file = None

		client_id = f"C{Consumer.static_counter}"
		Consumer.static_counter += 1
		self.client = mqtt.Client(client_id=client_id)
		self.client.on_connect = self._on_connect
		self.client.on_message = self._on_message

	def _on_connect(self, client, userdata, flags, reason_code, properties=None):
		if reason_code == 0:
			client.subscribe(self.args.topic, qos=self.args.qos)
			if self.args.verbose:
				print(f"[consumer] subscribed topic={self.args.topic}", flush=True)
		else:
			print(f"[consumer] connect failed rc={reason_code}", file=sys.stderr, flush=True)

	def _on_message(self, client, userdata, msg):
		try:
			record = json.loads(msg.payload.decode("utf-8"))
			ingest_time = utc_now_iso()
			record["ingest_time"] = ingest_time

			parsed_event_time = datetime.fromisoformat(record["event_time"].replace("Z", "+00:00"))
			parsed_ingest_time = datetime.fromisoformat(ingest_time.replace("Z", "+00:00"))
			record["pipeline_latency_ms"] = (parsed_ingest_time - parsed_event_time).total_seconds() * 1000

			self.out_file.write(json.dumps(record) + "\n")
			self.out_file.flush()
			self.metrics["consumed"] += 1

			if self.args.verbose:
				print(
					f"[consumer] wrote seq={record.get('seq')} latency_ms={record['pipeline_latency_ms']:.3f}",
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
			while not self.stop_flag["stop"]:
				time.sleep(0.2)
		finally:
			self.client.loop_stop()
			self.client.disconnect()
			self.out_file.close()
			append_jsonl_newline(self.out_path)
