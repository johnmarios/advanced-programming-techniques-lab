import json
import sys
import time

import paho.mqtt.client as mqtt

from labs.lab06.run_pipeline import create_event, create_run_id, epoch_to_utc_iso


class Producer:
    static_counter = 0

    def __init__(self, args, metrics, sampler, interpreter, stop_flag):
        self.args = args
        self.metrics = metrics
        self.sampler = sampler
        self.interpreter = interpreter
        self.stop_flag = stop_flag
        self.run_id = create_run_id()
        self.seq = 0

        client_id = f"P{Producer.static_counter}"
        Producer.static_counter += 1
        self.client = mqtt.Client(client_id=client_id)

    def produce(self):
        try:
            self.client.connect(self.args.broker, self.args.port, 60)
            self.client.loop_start()

            while not self.stop_flag["stop"]:
                try:
                    now = time.time()
                    raw = self.sampler.read()
                except Exception as exc:
                    print(f"[producer] sensor read error: {exc}", file=sys.stderr)
                    time.sleep(self.args.sample_interval)
                    continue

                for event in self.interpreter.update(raw, now):
                    self.seq += 1
                    event_time = epoch_to_utc_iso(event["t"])
                    state = "detected" if event.get("kind") == "motion_detected" else str(event.get("kind", "unknown"))

                    record = create_event(
                        event_time=event_time,
                        device_id=self.args.device_id,
                        wastebin_id=self.args.wastebin_id,
                        environment_id=self.args.environment_id,
                        event_type="motion",
                        motion_state=state,
                        seq=self.seq,
                        run_id=self.run_id,
                        context_iri=self.args.context,
                    )

                    payload = json.dumps(record)
                    result = self.client.publish(self.args.topic, payload, qos=self.args.qos)
                    if result.rc == mqtt.MQTT_ERR_SUCCESS:
                        self.metrics["produced"] += 1
                        if self.args.verbose:
                            print(
                                f"[producer] published seq={self.seq} topic={self.args.topic} "
                                f"state={record['motion_state']} event_time={event_time}",
                                flush=True,
                            )
                    else:
                        self.metrics["dropped"] += 1
                        if self.args.verbose:
                            print(
                                f"[producer] publish failed seq={self.seq} rc={result.rc}",
                                file=sys.stderr,
                                flush=True,
                            )

                time.sleep(self.args.sample_interval)
        finally:
            self.client.loop_stop()
            self.client.disconnect()