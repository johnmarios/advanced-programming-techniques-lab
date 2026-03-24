# Tests - run_pipeline.py

## Test 1 - No delay

### Command:
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

### Output:
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

### Logged in JSON fille:
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

### Conclusion:
Consumer instantly logs what is produced.

## Test 2 - small delay(10s)

### Command:
```bash
python run_pipeline.py \
  --device-id pir-01 \
  --pin 17 \
  --sample-interval 0.1 \
  --cooldown 5 \
  --min-high 0.2 \
  --queue-size 10 \
  --consumer-delay 10 \
  --duration 60 \
  --out motion_pipeline.jsonl \
  --verbose
```

### Output:
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

### Logged in JSON fille:
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

### Conclusion:
Consumer delays consumption of produced values, max_queue reaches 3. The producer stops working after 60s but consumer continues until everything is consumed.

## Test 3 - big delay(20s) + queue-size reduction(10-->5)

### Commmand:
```bash
python run_pipeline.py \
  --device-id pir-01 \
  --pin 17 \
  --sample-interval 0.1 \
  --cooldown 5 \
  --min-high 0.2 \
  --queue-size 5 \
  --consumer-delay 20 \
  --duration 60 \
  --out motion_pipeline.jsonl \
  --verbose
```

### Output:
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

### Logged in JSON fille:
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

### Conclusion:
Max_queue reaches queue size (5) and last measurement is dropped.

## Test 4 - big delay(20s) + queue-size reduction(5-->2)

### Command:
```bash
python run_pipeline.py \
  --device-id pir-01 \
  --pin 17 \
  --sample-interval 0.1 \
  --cooldown 5 \
  --min-high 0.2 \
  --queue-size 2 \
  --consumer-delay 20 \
  --duration 60 \
  --out motion_pipeline.jsonl \
  --verbose
```

### Output:
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

### Logged in JSON fille:
```
{"event_time": "2026-03-14T20:37:14.398Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 1, "run_id": "afcfd1a9-ae5f-4408-b399-75592303ae0b", "ingest_time": "2026-03-14T20:37:14.399Z", "pipeline_latency_ms": 1.0}
{"event_time": "2026-03-14T20:37:22.304Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 2, "run_id": "afcfd1a9-ae5f-4408-b399-75592303ae0b", "ingest_time": "2026-03-14T20:37:34.399Z", "pipeline_latency_ms": 12095.0}
{"event_time": "2026-03-14T20:37:30.610Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 3, "run_id": "afcfd1a9-ae5f-4408-b399-75592303ae0b", "ingest_time": "2026-03-14T20:37:54.399Z", "pipeline_latency_ms": 23789.0}
{"event_time": "2026-03-14T20:37:37.215Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 4, "run_id": "afcfd1a9-ae5f-4408-b399-75592303ae0b", "ingest_time": "2026-03-14T20:38:14.399Z", "pipeline_latency_ms": 37184.0}
{"event_time": "2026-03-14T20:37:54.727Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 7, "run_id": "afcfd1a9-ae5f-4408-b399-75592303ae0b", "ingest_time": "2026-03-14T20:38:34.399Z", "pipeline_latency_ms": 39672.0}
```

### Conclusion:
max_queue reaches queue size (2) and 4 measurements are dropped.

## Test 5 (RQ14) - consumer-delay 0.5

### Command:
```bash
python run_pipeline.py \
  --device-id pir-01 \
  --pin 17 \
  --sample-interval 0.1 \
  --cooldown 5 \
  --min-high 0.2 \
  --queue-size 2 \
  --consumer-delay 0.5 \
  --duration 60 \
  --out motion_pipeline.jsonl \
  --verbose
```

### Output:
```
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
[consumer] wrote seq=2 latency_ms=0.000
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[status] produced=2 consumed=2 dropped=0 queue=0 max_queue=1
[producer] queued seq=3 state=detected event_time=2026-03-14T20:54:11.809Z
[consumer] wrote seq=3 latency_ms=0.000
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[status] produced=3 consumed=3 dropped=0 queue=0 max_queue=1
[producer] queued seq=4 state=detected event_time=2026-03-14T20:54:18.714Z
[consumer] wrote seq=4 latency_ms=0.000
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[status] produced=4 consumed=4 dropped=0 queue=0 max_queue=1
[producer] queued seq=5 state=detected event_time=2026-03-14T20:54:23.718Z
[consumer] wrote seq=5 latency_ms=0.000
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[status] produced=5 consumed=5 dropped=0 queue=0 max_queue=1
[producer] queued seq=6 state=detected event_time=2026-03-14T20:54:29.522Z
[consumer] wrote seq=6 latency_ms=0.000
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[status] produced=6 consumed=6 dropped=0 queue=0 max_queue=1
[producer] queued seq=7 state=detected event_time=2026-03-14T20:54:36.126Z
[consumer] wrote seq=7 latency_ms=0.000
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[status] produced=7 consumed=7 dropped=0 queue=0 max_queue=1
[producer] queued seq=8 state=detected event_time=2026-03-14T20:54:41.130Z
[consumer] wrote seq=8 latency_ms=0.000
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[status] produced=8 consumed=8 dropped=0 queue=0 max_queue=1
[producer] queued seq=9 state=detected event_time=2026-03-14T20:54:47.334Z
[consumer] wrote seq=9 latency_ms=0.000
[status] produced=9 consumed=9 dropped=0 queue=0 max_queue=1
[status] produced=9 consumed=9 dropped=0 queue=0 max_queue=1
[status] produced=9 consumed=9 dropped=0 queue=0 max_queue=1
[status] produced=9 consumed=9 dropped=0 queue=0 max_queue=1
[status] produced=9 consumed=9 dropped=0 queue=0 max_queue=1
[logger] done. produced=9 consumed=9 dropped=0 max_queue=1
```

### Logged in JSON fille:
```
{"event_time": "2026-03-14T20:53:53.897Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 1, "run_id": "d71714ed-626b-4d13-b2da-6223e7f1f2c6", "ingest_time": "2026-03-14T20:53:53.898Z", "pipeline_latency_ms": 1.0}
{"event_time": "2026-03-14T20:54:04.404Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 2, "run_id": "d71714ed-626b-4d13-b2da-6223e7f1f2c6", "ingest_time": "2026-03-14T20:54:04.404Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:54:11.809Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 3, "run_id": "d71714ed-626b-4d13-b2da-6223e7f1f2c6", "ingest_time": "2026-03-14T20:54:11.809Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:54:18.714Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 4, "run_id": "d71714ed-626b-4d13-b2da-6223e7f1f2c6", "ingest_time": "2026-03-14T20:54:18.714Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:54:23.718Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 5, "run_id": "d71714ed-626b-4d13-b2da-6223e7f1f2c6", "ingest_time": "2026-03-14T20:54:23.718Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:54:29.522Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 6, "run_id": "d71714ed-626b-4d13-b2da-6223e7f1f2c6", "ingest_time": "2026-03-14T20:54:29.522Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:54:36.126Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 7, "run_id": "d71714ed-626b-4d13-b2da-6223e7f1f2c6", "ingest_time": "2026-03-14T20:54:36.126Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:54:41.130Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 8, "run_id": "d71714ed-626b-4d13-b2da-6223e7f1f2c6", "ingest_time": "2026-03-14T20:54:41.130Z", "pipeline_latency_ms": 0.0}
{"event_time": "2026-03-14T20:54:47.334Z", "device_id": "pir-01", "event_type": "motion", "motion_state": "detected", "seq": 9, "run_id": "d71714ed-626b-4d13-b2da-6223e7f1f2c6", "ingest_time": "2026-03-14T20:54:47.334Z", "pipeline_latency_ms": 0.0}
```

### Conclusion:
Nothing changed, the delay is too small.
