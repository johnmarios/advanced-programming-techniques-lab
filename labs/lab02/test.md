# Mini Tests

## Test 1 – Smoke test

Command:
```bash
python pir_smoke_test.py
```

Expected:

Prints "Motion Detected" when motion is detected

Output snippet:

```
Motion Detected
Motion stopped
Motion Detected
Motion stopped
Motion Detected
Motion stopped
```


## Test 2 – Pir_print.py

Command:
```bash
--pin 17 --sample-interval 0.1 --cooldown 5 --min-high 0.2 --duration 60
```
Expected:

Prints only interpreted events 

Output snippet:
```
t=   0.20s motion_detected
t=  16.31s motion_detected
t=  35.52s motion_detected
t=  54.63s motion_detected
```

## Test 3 – Pir_print.py with minimum time delay

Command:
```bash
--pin 17 --sample-interval 0.1 --cooldown 5 --min-high 0.2 --duration 60
```
Expected:

Prints only interpreted events but in shorter intervals than test 2.

Output snippet:
```
  t=   3.40s motion_detected
  t=  11.61s motion_detected
  t=  18.01s motion_detected
  t=  25.12s motion_detected
  t=  30.82s motion_detected
  t=  38.93s motion_detected
  t=  46.33s motion_detected
  t=  53.74s motion_detected
  t=  59.64s motion_detected
```

## Test 4 – Basic logger run

Command:

```bash
--device-id pir-01   --pin 17   --sample-interval 0.1   --cooldown 5   --min-high 0.2   --duration 60   --out motion_events.jso
nl   --verbose
```
Expected:
Motion events should be logged when movement is detected.

Output snippet:
```
[logger] seq=1 event_time=2026-03-09T18:12:55.407Z ingest_time=2026-03-09T18:12:55.407Z
[logger] seq=2 event_time=2026-03-09T18:13:02.111Z ingest_time=2026-03-09T18:13:02.111Z
[logger] seq=3 event_time=2026-03-09T18:13:07.815Z ingest_time=2026-03-09T18:13:07.815Z
[logger] seq=4 event_time=2026-03-09T18:13:13.722Z ingest_time=2026-03-09T18:13:13.722Z
[logger] seq=5 event_time=2026-03-09T18:13:19.125Z ingest_time=2026-03-09T18:13:19.125Z
[logger] seq=6 event_time=2026-03-09T18:13:24.729Z ingest_time=2026-03-09T18:13:24.729Z
[logger] seq=7 event_time=2026-03-09T18:13:31.233Z ingest_time=2026-03-09T18:13:31.233Z
[logger] seq=8 event_time=2026-03-09T18:13:36.937Z ingest_time=2026-03-09T18:13:36.937Z
[logger] seq=9 event_time=2026-03-09T18:13:44.042Z ingest_time=2026-03-09T18:13:44.042Z
[logger] seq=10 event_time=2026-03-09T18:13:49.546Z ingest_time=2026-03-09T18:13:49.546Z
[logger] seq=11 event_time=2026-03-09T18:13:54.849Z ingest_time=2026-03-09T18:13:54.849Z
[logger] done. run_id=cfa17779-11e9-445d-8231-6d9029059e0c records_written=11
```


