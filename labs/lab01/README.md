# Advanced Programming Techniques Lab

## Team Information
Repository created by Giannis Marios Papadopoulos.  
The rest of the team joined as invited collaborators.

Members: 
Marios Ioannis Papadopoulos 1092834
Filippos Theologos 1092633
Xristina Tzouda 1097346

---

# A. Network & SSH Setup

## RQ1
Hostname: `iotlab_upat_6`  
IP: `192.168.137.222`

## RQ2
The first SSH connection attempt failed with:

`ssh: connect to host 192.168.137.222 port 22: Connection refused`

This happened because the SSH service was not enabled yet on the Raspberry Pi.  
After enabling SSH through `raspi-config`, the connection succeeded.

## RQ3
Connection type: Wireless.

## RQ4
Enabled SSH using:
`raspi-config → Interface Options → SSH → Yes`

## RQ5
Command:
```bash
systemctl status ssh
```
Result: **active (running)**

## RQ6
We enabled SSH to work remotely on the Raspberry Pi from our laptop.

---

# B1

## RQ7
```bash
ssh iotlab_upat_6@192.168.137.222
```

## RQ8
The first time we connect, we receive the server’s public key (fingerprint) to verify that we are connecting to the correct server and not a fake one.

## RQ9
`uptime` shows how long the remote machine has been running.  
It is important to check system availability and status.

## RQ10
We generated SSH keys:

```bash
ssh-keygen -t rsa
```

This created the key pair in:
```
/home/iotlab_upat_6/.ssh/id_rsa
```

Then we copied the public key:

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub iotlab_upat_6@192.168.137.222
```

This allows login without entering a password.

## RQ11
SSH keys are easier and more secure.

---

# C0

## RQ12
We verified system time using:
```bash
date
```
The system time was correct.

## RQ13
Disk usage: 3.5GB.  
Disk usage is important because logs continuously grow and can fill system storage.

## RQ14
Python version: 3.13.5.  
Different Python versions may change language behavior and affect reproducibility.

---

# D1

## RQ15
The repository was created by Giannis Marios Papadopoulos and collaborators were added by invitation.

## RQ16
Without version control, it would be difficult to track each member’s contributions.

## RQ17
- `git add`: prepares changes to be recorded.
- `git commit`: records the changes locally.

## RQ18
`git push`: uploads local commits to the remote repository.  
It is important because it shares work with teammates.

## RQ19
If two teammates edit the same file without pulling first, a merge conflict may occur.

## RQ20
Yes, we use branches:

```bash
git checkout -b lab01/teammate1
```

All task changes are committed and pushed to this branch.  
Before merging, we run:

```bash
git pull origin main
```

When complete, we merge into `main`.

## RQ21
A merge conflict happens when two teammates change the same lines (or overlapping nearby lines) and Git cannot auto-merge. It usually appears if someone works without pulling recent remote changes first.

## RQ22
We used SSH key authentication.  
It is secure because credentials are not sent over the network and we do not need to enter a password every time.

## RQ23
Virtual environments should not be committed because:
- They are large.
- They contain unnecessary files.
- They may cause OS conflicts.

## RQ24
Logs should not be committed because:
- They constantly change.
- They may contain sensitive information.

## RQ25
We created the `advanced-programming-techniques-lab` folder on the Pi to keep our work organized.

## RQ26
Python path:
```
/home/iotlab_upat_6/advanced-programming-techniques-lab/labs/lab01/venv/bin/python
```

The path includes the `venv` folder, proving we are using the virtual environment.

## RQ27
A virtual environment creates an isolated Python environment with its own interpreter and packages.  
This allows each project to manage dependencies independently and ensures reproducibility.

## RQ28
We used `argparse` for CLI parsing.

`argparse` is part of Python’s standard library, so it does NOT need to be included in `requirements.txt`.

If we had used `click`, we would need to include it in `requirements.txt` because it is a third-party dependency.

## RQ29
- Using different dependency versions in `requirements.txt` can cause **inconsistent behavior** across environments.
- Code may work for one team but fail for another.
- Installation conflicts can occur.
- Runtime errors may arise due to API changes or behavior differences between versions.
- Security risks increase if some teams use outdated or unpatched dependencies.
- Overall maintenance, debugging, and collaboration become more complex over time.
  
## RQ30
- `pip list`  
  Shows all installed packages in the currently active environment.  
  If the venv is activated, it lists only the packages inside the venv.

- `pip show <package_name>`  
  Displays detailed information about a specific package.  
  Check the **Location** field to confirm it points to the venv directory and not the system Python.


## F.1 / F.2

## RQ31
A mock event generator lets us test the software workflow first (CLI, validation, logging, and reliability) before adding real hardware complexity.

## RQ32
With this mock we can test CLI validation, JSONL formatting, append-only logging, required fields, sequencing, timestamps, and counter behavior without using sensors.

## RQ33
`deposit` shows usage, while `heartbeat` shows liveness; separating them helps monitoring distinguish “idle” from “offline.”

## RQ34
If `heartbeat` events are missing, a monitoring system could incorrectly assume the device is offline, even if it is simply idle and functioning correctly.

## F.3

## RQ35
We added `--starting-total`, `--deposit-delta`, and `--verbose`: `--starting-total` sets the initial counter, `--deposit-delta` controls the increment step for accepted deposits, and `--verbose` prints progress every 5 records.

## RQ36
Failing early avoids bad logs and makes errors clear before execution continues.

## F.4 / F.5 

## RQ37
JSON Lines is ideal because each event is independent, appending is safe, and large files can be read line by line.

## RQ38
`seq` gives exact order and timestamps give time context, so together they improve traceability and debugging.

## RQ39
It keeps state consistent and prevents incorrect totals over time.

## RQ40
Checking that `deposit_total` changes correctly in long logs is hardest manually, because you must verify every step.

## F.6

## RQ41
If operational text is mixed into event logs, parsers fail and the JSONL format breaks.

## RQ42
Operational logs are useful to track progress and diagnose runtime problems quickly.

## F.7 / F.8 

## RQ43
This distinction allows our system to differentiate between incorrect user input and system-level failures.

## RQ44
Consistent exit codes let automation detect error type, retry when appropriate, and trigger the right alerts.

## RQ45
Without interrupt handling, writes may be incomplete, buffers may not flush, and troubleshooting becomes harder.

## G.1

## RQ46
Test command used:
```bash
python event_generator.py --device-id wastebin-01 --event-type deposit --count 5 --interval 0 --out test_events.log
```

First record:
```json
{"event_time": "2026-02-28T21:35:11.458Z", "ingest_time": "2026-02-28T21:35:11.459Z", "device_id": "wastebin-01", "event_type": "deposit", "seq": 1, "run_id": "4fd96845-d1a2-4451-a0c4-29e6db8473e8", "deposit_delta": 1, "deposit_total": 1, "status": "accepted"}
```

Last record:
```json
{"event_time": "2026-02-28T21:35:12.259Z", "ingest_time": "2026-02-28T21:35:12.259Z", "device_id": "wastebin-01", "event_type": "deposit", "seq": 5, "run_id": "4fd96845-d1a2-4451-a0c4-29e6db8473e8", "deposit_delta": 1, "deposit_total": 5, "status": "accepted"}
```

`seq` increased from 1 to 5, such as `deposit_total`  because deposits were accepted because of the previous event: `lid_open`. We also don't have `maintenance` event active. 

## RQ47
A consumer can check `event_type`, `status == "online"` is for heartbeats, and deposit fields for deposits.

## RQ48
Invalid command 1:
```bash
python event_generator.py --device-id wastebin-01 --event-type invalid_type --count 5 --interval 0 --out events.log
```
Error:
```text
Error: --event-type must be 'deposit', 'heartbeat', 'lid_open', 'lid_close', 'lid_clear', 'maintenance', or 'maintenance_termination'
```
Exit code: `2`

Invalid command 2:
```bash
python event_generator.py --device-id wastebin-01 --event-type heartbeat --count 0 --interval 0 --out events.log
```
Error:
```text
Error: --count must be > 0
```
Exit code: `2`

## RQ49
`--count 0` is probably most common, because users often run quick tests and accidentally set zero.

## RQ50
In the Ctrl-C test (`--count 100`, `--interval 0.2`), 33 records were written before interruption.
**Interrupted. Wrote 33 record(s).**

## H.3







