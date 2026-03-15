# Advanced Programming Techniques Lab
## Team Information
Members: 
- Marios Ioannis Papadopoulos 1092834
- Filippos Theologos 1092633
- Xristina Tzouda 1097346

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




















