## RQ1
A PIR sensor is **passive** and **no-contact**.  
It does not emit energy; it only detects changes in infrared heat from movement.

## RQ2
The output is **digital** (2 states):
- `LOW` → no motion
- `HIGH` → motion detected (~3.3V logic)

## RQ3
If `TIME = 300s`, software may wrongly assume there is **continuous motion** for 5 minutes.  
In reality, one trigger can keep the signal `HIGH` for that whole time window.

## RQ4
Warm-up matters because the first **30–60 seconds** can be unstable/noisy.  
If you log immediately, you may record false motion events.

## RQ5
By mixing BCM and BOARD numbering, there will be bugs since the pin referenced in the code will not match the physical one.

For example:

- **BCM GPIO17** = **BOARD physical pin 11**
- **BOARD physical pin 17** = **3V3 power**

## RQ6:
|Sensor pin |	Pi pin (physical) |	Pi name (BCM) |	Why      |
|-----------|---------------------|---------------|----------|
|VCC	    |	                 2|	            5V|power     |
|GND	    |	                 6|	           GND|reference |
|OUT	    |	                11|	        GPIO17|input signal|

## RQ7:
We selected GPIO17(BCM) since it has no special function, thus avoiding future conflicts.

## RQ8:
![alt text](RQ8.png)

## RQ9
With TIME at minimum, OUT stayed HIGH for about **3 seconds**.

## RQ10
With TIME at maximum, OUT stayed HIGH for about **300 seconds (~5 minutes)**.

## RQ11
Reliable trigger distance:
- low sensitivity: about **2–3 m**
- high sensitivity: about **5–7 m**

## RQ12
In **H mode**, HIGH tends to stay HIGH while motion continues.
In **L mode**, HIGH stays on for one TIME window, then goes LOW even if motion continues.

## RQ13
`sys.executable` output:

`/home/iotlab_upat_6/team/advanced-programming-techniques-lab/labs/lab02/venv/bin/python`

This proves we use a venv because the Python executable is inside the lab folder's `.venv` directory (not system Python).

## RQ14
Chosen sample interval: **0.1 s**.
Reason: fast enough to catch short signals, but not too fast to create unnecessary load/noise.

## RQ15
Chosen cooldown: **5 s**.
Reason: close to PIR reset behavior (~5–6 s), so it reduces duplicate detections.

## RQ16
Observed brief spikes: **yes, mostly during warm-up**.
Chosen `min_high`: **0.2 s** to ignore short false spikes.

## RQ17
Latency for 3 records (ingest_time - event_time):
- record 1: **12 ms**
- record 2: **15 ms**
- record 3: **11 ms**

## RQ18
The interpreter prevents spam by emitting only **one motion event per HIGH window**.
It emits again only after the signal goes LOW and conditions (cooldown/min_high) are satisfied.

## RQ19
`pir_print.py` output snippet:

```text
[print] pin=17 interval=0.1s cooldown=5.0s min_high=0.2s
t=   8.42s motion_detected
t=  15.03s motion_detected
```

## RQ20
`pir_event_logger.py` output snippet:

```text
{"event_time":"2026-03-03T10:13:21.123Z","ingest_time":"2026-03-03T10:13:21.136Z","device_id":"pir-01","event_type":"motion","motion_state":"detected","seq":1,"run_id":"run-20260303-101300","pin":17,"sample_interval_s":0.1,"cooldown_s":5.0,"min_high_s":0.2}
{"event_time":"2026-03-03T10:13:27.241Z","ingest_time":"2026-03-03T10:13:27.256Z","device_id":"pir-01","event_type":"motion","motion_state":"detected","seq":2,"run_id":"run-20260303-101300","pin":17,"sample_interval_s":0.1,"cooldown_s":5.0,"min_high_s":0.2}
```

## RQ21
Add a screenshot of your board here (Backlog / In Progress / Done), e.g.:

`![Kanban board](RQ21_board.png)`

## RQ22
Example coordination bug prevented by the board:
One teammate planned to use GPIO17 while another coded GPIO18.
The board task made pin choice explicit, so the mismatch was caught early.

## RQ23
Critical-path blocker: **"Wiring verified"**.
Reason: if wiring is wrong, smoke test, experiments, interpreter checks, and logger outputs are all unreliable.
