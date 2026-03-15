# Advanced Programming Techniques Lab
## Team Information
Members: 
- Marios Ioannis Papadopoulos 1092834
- Filippos Theologos 1092633
- Xristina Tzouda 1097346


---
# SECTION A - RUNBOOK 
## Nesessary hardware and software from previous labs
- Hardware:
  - Raspberry Pi 5
  - HC-SR501 PIR motion sensor
  - Jumper wires(female to female)
- Wiring the sensor:
  Use the example given on lab02, made sure to connect the OUT on the same pin.
- Connection
  As shown in lab01, in order to run the following code it's nesessary to connect to the raspberry pi 5 via ssh. Clear instructions can be found on lab01.
- Software:
  - The PIR sensor logic (`sampler.py`, `interpreter.py`) is reused from Lab 02 and placed inside `pirlib/`. We moved the file to lab03 and run the pipeline based on this stracture.
  - Use a venv just like lab01 and lab02.
  - Make sure to inastall a `requirments.txt` and use it exactly like lab02.

## The code 
# No delay test
- Consumer instantly consumes what is produced.
- Run the following on bash
```bash
      python run_pipeline.py \
      --device-id pir-01 \
      --pin 17 \
      --sample-interval 0.1 \
      --cooldown 5 \
      --min-high 0.2 \
      --queue-size 100 \
      --consumer-delay 0.0 \
      --duration 60 \
      --out motion_pipeline.jsonl \
      --verbose
```
- Result
 ```
  [logger] device=pir-01 pin=17 interval=0.1s cooldown=5.0s min_high=0.2s duration=60.0s out=motion_pipeline.jsonl
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[producer] queued seq=1 state=detected event_time=2026-03-14T20:09:54.980Z
[consumer] wrote seq=1 latency_ms=0.000
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[producer] queued seq=2 state=detected event_time=2026-03-14T20:10:02.088Z
[consumer] wrote seq=2 latency_ms=0.000
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[producer] queued seq=3 state=detected event_time=2026-03-14T20:10:07.194Z
[consumer] wrote seq=3 latency_ms=1.000
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[producer] queued seq=4 state=detected event_time=2026-03-14T20:10:15.404Z
[consumer] wrote seq=4 latency_ms=0.000
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[producer] queued seq=5 state=detected event_time=2026-03-14T20:10:22.512Z
[consumer] wrote seq=5 latency_ms=0.000
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[producer] queued seq=6 state=detected event_time=2026-03-14T20:10:28.518Z
[consumer] wrote seq=6 latency_ms=0.000
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[producer] queued seq=7 state=detected event_time=2026-03-14T20:10:35.425Z
[consumer] wrote seq=7 latency_ms=0.000
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[producer] queued seq=8 state=detected event_time=2026-03-14T20:10:42.632Z
[consumer] wrote seq=8 latency_ms=0.000
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[producer] queued seq=9 state=detected event_time=2026-03-14T20:10:49.139Z
[consumer] wrote seq=9 latency_ms=0.000
[status] produced=9 consumed=9 dropped=0 queue=0 max_queue=1
[status] produced=9 consumed=9 dropped=0 queue=0 max_queue=1
[status] produced=9 consumed=9 dropped=0 queue=0 max_queue=1
[logger] done. produced=9 consumed=9 dropped=0 max_queue=1
```
- JSON file
```
{"event_time": "2026-03-14T20:09:54.980Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 1, "run_id": "7b496f39-408b-4f00-9287-b14a3416eae4", "ingest_time": "2026-03-14T20:09:54.980Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:10:02.088Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 2, "run_id": "7b496f39-408b-4f00-9287-b14a3416eae4", "ingest_time": "2026-03-14T20:10:02.088Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:10:07.194Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 3, "run_id": "7b496f39-408b-4f00-9287-b14a3416eae4", "ingest_time": "2026-03-14T20:10:07.195Z", "pipeline_latency_ms": 1.0}
{"event_time": "2026-03-14T20:10:15.404Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 4, "run_id": "7b496f39-408b-4f00-9287-b14a3416eae4", "ingest_time": "2026-03-14T20:10:15.404Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:10:22.512Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 5, "run_id": "7b496f39-408b-4f00-9287-b14a3416eae4", "ingest_time": "2026-03-14T20:10:22.512Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:10:28.518Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 6, "run_id": "7b496f39-408b-4f00-9287-b14a3416eae4", "ingest_time": "2026-03-14T20:10:28.518Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:10:35.425Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 7, "run_id": "7b496f39-408b-4f00-9287-b14a3416eae4", "ingest_time": "2026-03-14T20:10:35.425Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:10:42.632Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 8, "run_id": "7b496f39-408b-4f00-9287-b14a3416eae4", "ingest_time": "2026-03-14T20:10:42.632Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:10:49.139Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 9, "run_id": "7b496f39-408b-4f00-9287-b14a3416eae4", "ingest_time": "2026-03-14T20:10:49.139Z", "pipeline_latency_ms": 0.0}
```
# Small delay(10s)
- Consumer delays consumption of produced values, max_queue reaches 3. The producer stops working after 60s but consumer continues until everything is consumed.
- Run :
```bash
python run_pipeline.py   --device-id pir-01   --pin 17   --sample-interval 0.1   --cooldown 5   --min-high 0.2   --queue-size 10   --consumer-delay 10   --d
uration 60   --out motion_pipeline.jsonl   --verbose
```
- Result :
```
[logger] device=pir-01 pin=17 interval=0.1s cooldown=5.0s min_high=0.2s duration=60.0s out=motion_pipeline.jsonl
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[producer] queued seq=1 state=detected event_time=2026-03-14T20:11:18.429Z
[consumer] wrote seq=1 latency_ms=0.000
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[producer] queued seq=2 state=detected event_time=2026-03-14T20:11:24.935Z
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[consumer] wrote seq=2 latency_ms=3494.000
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[producer] queued seq=3 state=detected event_time=2026-03-14T20:11:32.643Z
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=1
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=1
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=1
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=1
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=1
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=1
[consumer] wrote seq=3 latency_ms=5787.000
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[producer] queued seq=4 state=detected event_time=2026-03-14T20:11:39.450Z
[status] produced=4 consumed=3 dropped=0 queue=1 max_queue=1
[status] produced=4 consumed=3 dropped=0 queue=1 max_queue=1
[status] produced=4 consumed=3 dropped=0 queue=1 max_queue=1
[status] produced=4 consumed=3 dropped=0 queue=1 max_queue=1
[status] produced=4 consumed=3 dropped=0 queue=1 max_queue=1
[status] produced=4 consumed=3 dropped=0 queue=1 max_queue=1
[producer] queued seq=5 state=detected event_time=2026-03-14T20:11:45.254Z
[status] produced=5 consumed=3 dropped=0 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=0 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=0 queue=2 max_queue=2
[consumer] wrote seq=4 latency_ms=8980.000
[status] produced=5 consumed=4 dropped=0 queue=1 max_queue=2
[status] produced=5 consumed=4 dropped=0 queue=1 max_queue=2
[status] produced=5 consumed=4 dropped=0 queue=1 max_queue=2
[status] produced=5 consumed=4 dropped=0 queue=1 max_queue=2
[status] produced=5 consumed=4 dropped=0 queue=1 max_queue=2
[producer] queued seq=6 state=detected event_time=2026-03-14T20:11:53.660Z
[status] produced=6 consumed=4 dropped=0 queue=2 max_queue=2
[status] produced=6 consumed=4 dropped=0 queue=2 max_queue=2
[status] produced=6 consumed=4 dropped=0 queue=2 max_queue=2
[status] produced=6 consumed=4 dropped=0 queue=2 max_queue=2
[status] produced=6 consumed=4 dropped=0 queue=2 max_queue=2
[consumer] wrote seq=5 latency_ms=13176.000
[status] produced=6 consumed=5 dropped=0 queue=1 max_queue=2
[status] produced=6 consumed=5 dropped=0 queue=1 max_queue=2
[producer] queued seq=7 state=detected event_time=2026-03-14T20:12:00.765Z
[status] produced=7 consumed=5 dropped=0 queue=2 max_queue=2
[status] produced=7 consumed=5 dropped=0 queue=2 max_queue=2
[status] produced=7 consumed=5 dropped=0 queue=2 max_queue=2
[status] produced=7 consumed=5 dropped=0 queue=2 max_queue=2
[status] produced=7 consumed=5 dropped=0 queue=2 max_queue=2
[status] produced=7 consumed=5 dropped=0 queue=2 max_queue=2
[status] produced=7 consumed=5 dropped=0 queue=2 max_queue=2
[producer] queued seq=8 state=detected event_time=2026-03-14T20:12:07.670Z
[status] produced=8 consumed=5 dropped=0 queue=3 max_queue=3
[consumer] wrote seq=6 latency_ms=14770.000
[status] produced=8 consumed=6 dropped=0 queue=2 max_queue=3
[status] produced=8 consumed=6 dropped=0 queue=2 max_queue=3
[status] produced=8 consumed=6 dropped=0 queue=2 max_queue=3
[status] produced=8 consumed=6 dropped=0 queue=2 max_queue=3
[producer] queued seq=9 state=detected event_time=2026-03-14T20:12:12.673Z
[status] produced=9 consumed=6 dropped=0 queue=3 max_queue=3
[status] produced=9 consumed=6 dropped=0 queue=3 max_queue=3
[consumer] wrote seq=7 latency_ms=17666.000
[consumer] wrote seq=8 latency_ms=20761.000
[consumer] wrote seq=9 latency_ms=25758.000
[logger] done. produced=9 consumed=9 dropped=0 max_queue=3
```
- JSON file
```
{"event_time": "2026-03-14T20:11:18.429Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 1, "run_id": "2b5c4e6f-6ca4-4756-bfe8-b2f8ef2be102", "ingest_time": "2026-03-14T20:11:18.429Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:11:24.935Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 2, "run_id": "2b5c4e6f-6ca4-4756-bfe8-b2f8ef2be102", "ingest_time": "2026-03-14T20:11:28.429Z", "pipeline_latency_ms": 3494.0}
{"event_time": "2026-03-14T20:11:32.643Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 3, "run_id": "2b5c4e6f-6ca4-4756-bfe8-b2f8ef2be102", "ingest_time": "2026-03-14T20:11:38.430Z", "pipeline_latency_ms": 5787.0}
{"event_time": "2026-03-14T20:11:39.450Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 4, "run_id": "2b5c4e6f-6ca4-4756-bfe8-b2f8ef2be102", "ingest_time": "2026-03-14T20:11:48.430Z", "pipeline_latency_ms": 8980.0}
{"event_time": "2026-03-14T20:11:45.254Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 5, "run_id": "2b5c4e6f-6ca4-4756-bfe8-b2f8ef2be102", "ingest_time": "2026-03-14T20:11:58.430Z", "pipeline_latency_ms": 13176.0}
{"event_time": "2026-03-14T20:11:53.660Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 6, "run_id": "2b5c4e6f-6ca4-4756-bfe8-b2f8ef2be102", "ingest_time": "2026-03-14T20:12:08.430Z", "pipeline_latency_ms": 14770.0}
{"event_time": "2026-03-14T20:12:00.765Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 7, "run_id": "2b5c4e6f-6ca4-4756-bfe8-b2f8ef2be102", "ingest_time": "2026-03-14T20:12:18.431Z", "pipeline_latency_ms": 17666.0}
{"event_time": "2026-03-14T20:12:07.670Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 8, "run_id": "2b5c4e6f-6ca4-4756-bfe8-b2f8ef2be102", "ingest_time": "2026-03-14T20:12:28.431Z", "pipeline_latency_ms": 20761.0}
{"event_time": "2026-03-14T20:12:12.673Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 9, "run_id": "2b5c4e6f-6ca4-4756-bfe8-b2f8ef2be102", "ingest_time": "2026-03-14T20:12:38.431Z", "pipeline_latency_ms": 25758.0}
```
# Big delay(20s) + queue-size reduction(10-5)-->max_queue reaches queue size (5) and last measurement dropped.
- Run :
```bash
python run_pipeline.py   --device-id pir-01   --pin 17   --sample-interval 0.1   --cooldown 5   --min-high 0.2   --queue-size 5   --consumer-delay 20   --du
ration 60   --out motion_pipeline.jsonl   --verbose
```
- Result :
```
[logger] device=pir-01 pin=17 interval=0.1s cooldown=5.0s min_high=0.2s duration=60.0s out=motion_pipeline.jsonl
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[producer] queued seq=1 state=detected event_time=2026-03-14T20:20:27.413Z
[consumer] wrote seq=1 latency_ms=0.000
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[producer] queued seq=2 state=detected event_time=2026-03-14T20:20:37.221Z
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[producer] queued seq=3 state=detected event_time=2026-03-14T20:20:44.627Z
[status] produced=3 consumed=1 dropped=0 queue=2 max_queue=2
[status] produced=3 consumed=1 dropped=0 queue=2 max_queue=2
[status] produced=3 consumed=1 dropped=0 queue=2 max_queue=2
[consumer] wrote seq=2 latency_ms=10192.000
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=2
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=2
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=2
[producer] queued seq=4 state=detected event_time=2026-03-14T20:20:50.431Z
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[producer] queued seq=5 state=detected event_time=2026-03-14T20:20:57.436Z
[status] produced=5 consumed=2 dropped=0 queue=3 max_queue=3
[status] produced=5 consumed=2 dropped=0 queue=3 max_queue=3
[status] produced=5 consumed=2 dropped=0 queue=3 max_queue=3
[status] produced=5 consumed=2 dropped=0 queue=3 max_queue=3
[status] produced=5 consumed=2 dropped=0 queue=3 max_queue=3
[producer] queued seq=6 state=detected event_time=2026-03-14T20:21:02.439Z
[status] produced=6 consumed=2 dropped=0 queue=4 max_queue=4
[status] produced=6 consumed=2 dropped=0 queue=4 max_queue=4
[status] produced=6 consumed=2 dropped=0 queue=4 max_queue=4
[status] produced=6 consumed=2 dropped=0 queue=4 max_queue=4
[status] produced=6 consumed=2 dropped=0 queue=4 max_queue=4
[consumer] wrote seq=3 latency_ms=22786.000
[status] produced=6 consumed=3 dropped=0 queue=3 max_queue=4
[producer] queued seq=7 state=detected event_time=2026-03-14T20:21:07.943Z
[status] produced=7 consumed=3 dropped=0 queue=4 max_queue=4
[status] produced=7 consumed=3 dropped=0 queue=4 max_queue=4
[status] produced=7 consumed=3 dropped=0 queue=4 max_queue=4
[status] produced=7 consumed=3 dropped=0 queue=4 max_queue=4
[status] produced=7 consumed=3 dropped=0 queue=4 max_queue=4
[producer] queued seq=8 state=detected event_time=2026-03-14T20:21:12.946Z
[status] produced=8 consumed=3 dropped=0 queue=5 max_queue=5
[status] produced=8 consumed=3 dropped=0 queue=5 max_queue=5
[status] produced=8 consumed=3 dropped=0 queue=5 max_queue=5
[status] produced=8 consumed=3 dropped=0 queue=5 max_queue=5
[status] produced=8 consumed=3 dropped=0 queue=5 max_queue=5
[producer] queue full, dropped seq=9
[status] produced=8 consumed=3 dropped=1 queue=5 max_queue=5
[status] produced=8 consumed=3 dropped=1 queue=5 max_queue=5
[status] produced=8 consumed=3 dropped=1 queue=5 max_queue=5
[status] produced=8 consumed=3 dropped=1 queue=5 max_queue=5
[status] produced=8 consumed=3 dropped=1 queue=5 max_queue=5
[status] produced=8 consumed=3 dropped=1 queue=5 max_queue=5
[status] produced=8 consumed=3 dropped=1 queue=5 max_queue=5
[consumer] wrote seq=4 latency_ms=36983.000
[consumer] wrote seq=5 latency_ms=49978.000
[consumer] wrote seq=6 latency_ms=64975.000
[consumer] wrote seq=7 latency_ms=79471.000
[consumer] wrote seq=8 latency_ms=94469.000
[logger] done. produced=8 consumed=8 dropped=1 max_queue=5
 ```
- JSON file :
```  
{"event_time": "2026-03-14T20:20:27.413Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 1, "run_id": "0f5c162e-8f44-4988-9aaf-3b391e02c858", "ingest_time": "2026-03-14T20:20:27.413Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:20:37.221Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 2, "run_id": "0f5c162e-8f44-4988-9aaf-3b391e02c858", "ingest_time": "2026-03-14T20:20:47.413Z", "pipeline_latency_ms": 10192.0}
{"event_time": "2026-03-14T20:20:44.627Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 3, "run_id": "0f5c162e-8f44-4988-9aaf-3b391e02c858", "ingest_time": "2026-03-14T20:21:07.413Z", "pipeline_latency_ms": 22786.0}
{"event_time": "2026-03-14T20:20:50.431Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 4, "run_id": "0f5c162e-8f44-4988-9aaf-3b391e02c858", "ingest_time": "2026-03-14T20:21:27.414Z", "pipeline_latency_ms": 36983.0}
{"event_time": "2026-03-14T20:20:57.436Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 5, "run_id": "0f5c162e-8f44-4988-9aaf-3b391e02c858", "ingest_time": "2026-03-14T20:21:47.414Z", "pipeline_latency_ms": 49978.0}
{"event_time": "2026-03-14T20:21:02.439Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 6, "run_id": "0f5c162e-8f44-4988-9aaf-3b391e02c858", "ingest_time": "2026-03-14T20:22:07.414Z", "pipeline_latency_ms": 64974.99999999999}
{"event_time": "2026-03-14T20:21:07.943Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 7, "run_id": "0f5c162e-8f44-4988-9aaf-3b391e02c858", "ingest_time": "2026-03-14T20:22:27.414Z", "pipeline_latency_ms": 79471.0}
{"event_time": "2026-03-14T20:21:12.946Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 8, "run_id": "0f5c162e-8f44-4988-9aaf-3b391e02c858", "ingest_time": "2026-03-14T20:22:47.415Z", "pipeline_latency_ms": 94469.0}
```
# Big delay(20s) + queue-size reduction(5->2)-->max_queue reaches queue size (2) and 4 measurements are dropped
- Run :
```bash
 python run_pipeline.py   --device-id pir-01   --pin 17   --sample-interval 0.1   --cooldown 5   --min-high 0.2   --queue-size 2   --consumer-delay 20   --du
ration 60   --out motion_pipeline.jsonl   --verbose
```
- Result :
```          
[logger] device=pir-01 pin=17 interval=0.1s cooldown=5.0s min_high=0.2s duration=60.0s out=motion_pipeline.jsonl
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[producer] queued seq=1 state=detected event_time=2026-03-14T20:37:14.398Z
[consumer] wrote seq=1 latency_ms=1.000
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[producer] queued seq=2 state=detected event_time=2026-03-14T20:37:22.304Z
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[status] produced=2 consumed=1 dropped=0 queue=1 max_queue=1
[producer] queued seq=3 state=detected event_time=2026-03-14T20:37:30.610Z
[status] produced=3 consumed=1 dropped=0 queue=2 max_queue=2
[status] produced=3 consumed=1 dropped=0 queue=2 max_queue=2
[status] produced=3 consumed=1 dropped=0 queue=2 max_queue=2
[status] produced=3 consumed=1 dropped=0 queue=2 max_queue=2
[consumer] wrote seq=2 latency_ms=12095.000
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=2
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=2
[status] produced=3 consumed=2 dropped=0 queue=1 max_queue=2
[producer] queued seq=4 state=detected event_time=2026-03-14T20:37:37.215Z
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=0 queue=2 max_queue=2
[producer] queue full, dropped seq=5
[status] produced=4 consumed=2 dropped=1 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=1 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=1 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=1 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=1 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=1 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=1 queue=2 max_queue=2
[producer] queue full, dropped seq=6
[status] produced=4 consumed=2 dropped=2 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=2 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=2 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=2 queue=2 max_queue=2
[status] produced=4 consumed=2 dropped=2 queue=2 max_queue=2
[consumer] wrote seq=3 latency_ms=23789.000
[producer] queued seq=7 state=detected event_time=2026-03-14T20:37:54.727Z
[status] produced=5 consumed=3 dropped=2 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=2 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=2 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=2 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=2 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=2 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=2 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=2 queue=2 max_queue=2
[producer] queue full, dropped seq=8
[status] produced=5 consumed=3 dropped=3 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=3 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=3 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=3 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=3 queue=2 max_queue=2
[producer] queue full, dropped seq=9
[status] produced=5 consumed=3 dropped=4 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=4 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=4 queue=2 max_queue=2
[status] produced=5 consumed=3 dropped=4 queue=2 max_queue=2
[consumer] wrote seq=4 latency_ms=37184.000
[consumer] wrote seq=7 latency_ms=39672.000
[logger] done. produced=5 consumed=5 dropped=4 max_queue=2
```
- JSON file
```
{"event_time": "2026-03-14T20:37:14.398Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 1, "run_id": "afcfd1a9-ae5f-4408-b399-75592303ae0b", "ingest_time": "2026-03-14T20:37:14.399Z", "pipeline_latency_ms": 1.0}
{"event_time": "2026-03-14T20:37:22.304Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 2, "run_id": "afcfd1a9-ae5f-4408-b399-75592303ae0b", "ingest_time": "2026-03-14T20:37:34.399Z", "pipeline_latency_ms": 12095.0}
{"event_time": "2026-03-14T20:37:30.610Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 3, "run_id": "afcfd1a9-ae5f-4408-b399-75592303ae0b", "ingest_time": "2026-03-14T20:37:54.399Z", "pipeline_latency_ms": 23789.0}
{"event_time": "2026-03-14T20:37:37.215Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 4, "run_id": "afcfd1a9-ae5f-4408-b399-75592303ae0b", "ingest_time": "2026-03-14T20:38:14.399Z", "pipeline_latency_ms": 37184.0}
{"event_time": "2026-03-14T20:37:54.727Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 7, "run_id": "afcfd1a9-ae5f-4408-b399-75592303ae0b", "ingest_time": "2026-03-14T20:38:34.399Z", "pipeline_latency_ms": 39672.0}
```
## Command-Line Arguments - Explanation
- `--device-id` : Identifier for the sensor device --> `pir-01`
- `--pin` : GPIO pin number connected to the PIR sensor -->`17`
- `--sample-interval` : How often (in seconds) to read the sensor --> `0.1`
- `--cooldown` : Minimum seconds between two detected events --> `5`
- `--min-high` : Minimum seconds the signal must be HIGH to count --> `0.2`
- `--queue-size` : Maximum number of events held in the queue --> `100`
- `--consumer-delay` : Artificial delay (seconds) added per consumed event --> `0.0`
- `--duration` : Total run time in seconds --> `60`
- `--out` : Output JSONL file path --> `motion_pipeline.jsonl`
- `--verbose` : Print periodic status lines to the terminal --> flag 
## JSON FILE RECORDS - EXPLANATION
- `event_time` : The timestamp when the PIR sensor detected motion
- `device_id` : The identifier of the device
- `event_type` : The category of the event
- `motion_state` : The detected state
- ` seq` : A sequential counter for events within the current pipeline run
- `run_id` : Identify the entire pipeline run
- `ingest_time` : The timestamp when we actually wrote the record to the file
- `pipeline_latency_ms` : The difference (in ms) between `event_time` and `ingest_time` — the queue delay

---
# SECTION B - REPORT
# Architecture and reuse
## RQ1
In lab02 we implemented :
1. Collect by reading the PIR pin via the sampler.
2. Compute by turning raw signal samples into motion events.
3. Store by writing records to a log file.
## RQ2
`sampler.py` and `interpreter.py` were reused without modification.
## RQ3
The main loop is different from lab02. 
# Pipeline concepts
## RQ4
A queue acts like a waiting line for data, ensuring that fast data collection doesn’t overwhelm slower writing operations, while keeping the system stable and efficient.
## RQ5
Backpressure is a mechanism used to slow down or control the rate of data production when the consumer cannot keep up.
## RQ6
A slow writer can become a data acquisition problem because if data cannot be written fast enough, the system eventually runs out of space to hold incoming data, which interferes with the ability to keep collecting it.
# ETL and transformation
## RQ7
The pipeline is closer to ETL. 
The producer extracts raw signal data and immediately transforms it into a structured record before placing it on the queue. 
By the time the consumer writes to disk, the data has already been shaped. 
Loading (writing) happens after the transformation, not before.
## RQ8
The interpreter converts a raw boolean pin sample into a meaningful motion event.
## RQ9
Computing pipeline_latency_ms could be moved to a later stage. For example, a separate analytics service that reads the JSONL file and computes latency statistics in batch
# Implementation
## RQ10
The producer :
1. reads the PIR sensor
2. passes samples through the interpreter.
3. places structured motion event records onto the bounded queue
## RQ11
The consumer :
1. takes records from the queue
2. enriches each record with an ingest timestamp and pipeline latency
3. writes it as a single JSON line to the output file
## RQ12
- Record 1 :
{"event_time": "2026-03-14T20:09:54.980Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 1, "run_id": "7b496f39-408b-             4f00-9287-b14a3416eae4", "ingest_time": "2026-03-14T20:09:54.980Z", "pipeline_latency_ms": 0.0}
- Record 2 :
{"event_time": "2026-03-14T20:10:07.194Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 3, "run_id": "7b496f39-408b-            4f00-9287-b14a3416eae4", "ingest_time": "2026-03-14T20:10:07.195Z", "pipeline_latency_ms": 1.0}
- Explanation :
  - `event_time` : The timestamp when the PIR sensor detected motion
  - `device_id` : The identifier of the device
  - `event_type` : The category of the event
  - `motion_state` : The detected state
  - ` seq` : A sequential counter for events within the current pipeline run
  - `run_id` : Identify the entire pipeline run
  - `ingest_time` : The timestamp when we actually wrote the record to the file
  - `pipeline_latency_ms` : The difference (in ms) between `event_time` and `ingest_time` — the queue delay
## RQ13
Answered on RQ12
# Experimental observations
## RQ14
Nothing changed, the delay is too small
```
iotlab_upat_6@iotlab-Upat-6:~/team/advanced-programming-techniques-lab/labs/lab03 $ python run_pipeline.py   --device-id pir-01   --pin 17   --sample-interval 0.1   --cooldown 5   --min-high 0.2   --queue-size 2   --consumer-delay 0.5   --duration 60   --out motion_pipeline.jsonl   --verbose
[logger] device=pir-01 pin=17 interval=0.1s cooldown=5.0s min_high=0.2s duration=60.0s out=motion_pipeline.jsonl
[status] produced=0 consumed=0 dropped=0 queue=0 max_queue=0
[producer] queued seq=1 state=detected event_time=2026-03-14T20:53:53.897Z
[consumer] wrote seq=1 latency_ms=1.000
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[status] produced=1 consumed=1 dropped=0 queue=0 max_queue=1
[producer] queued seq=2 state=detected event_time=2026-03-14T20:54:04.404Z
```
## RQ15
No, the queue did not need to absorb any slowdown, because there was no real slowdown to absorb in this case.
## RQ16
The queue value grows and stays elevated in the status lines, and events start getting dropped
1. Example : high-delay test 
   ```[status] produced=4 consumed=1 dropped=2 queue=2 max_queue=2
2. Example : No delay test
   ```[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
## RQ17
A bounded queue is more informative because it forces the system to make a visible, measurable decision when it runs out of space.
An unbounded queue on the other hand just keeps silently accepting events, so from the outside everything looks fine, no drops, no errors.
1. Example of bounded queue - high delay test :
   ```[status] produced=4 consumed=1 dropped=2 queue=2 max_queue=2
   this makes it clear that our queue is full and events are being lost     
## RQ18

1. Status lines are for us:
   - They are diagnostic, real-time feedback meant to be read while the pipeline is running
   - They change every second and are only useful in the moment
   - They are unstructured text like the one shown on RQ17.
2. JSONL records are for machines :
  - They are structured, persistent data meant to be parsed, queried, or fed into other tools later
  - Every line must be a valid, clean JSON object like the example shown on RQ12

## RQ19
The `run_id` field, a unique UUID generated once per pipeline execution. Every time we run `run_pipeline.py`, a new `run_id` is generated. This means that even if all runs write to the same JSONL file, you can always tell which records belong to which execution.
## RQ20
Because the Raspberry pi has very limited memory and an unbounded queue would consume it without giving us error or any other indication.
## RQ21
The part that detects motion events, timestamps them, and pushes them onto the queue could stay almost completely unchanged because it's job is to detect a motion event from the PIR sensor, create a structured record and then put it on the queue. It has no knowledge of what happens after that, whether we use a JSONL file or not.











