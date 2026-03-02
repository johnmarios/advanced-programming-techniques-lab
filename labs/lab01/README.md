# Advanced Programming Techniques Lab

## Team Information
Repository created by Giannis Marios Papadopoulos.  
The rest of the team joined as invited collaborators.

Members: 
Marios Ioannis Papadopoulos 1092834
Filippos Theologos 1092633
Xristina Tzouda 1097346

---
# SECTION A - RUNBOOK
# Part-A. One-time Raspberry Pi bootstrap
## 0. Necessary hardware and apps 
- Raspberry Pi 5
- Laptop with SSH and Git installed
- GitHub account
- Python 3.9+ on the Raspberry Pi
- Internet access
- Open the hotspot from a laptop and connect on th raspberry pi

## 1. Boot, network, and identity
On the Raspberry Pi :
```bash
hostname
ip a
ping -c 3 8.8.8.8
ping -c 3 google.com .
```
Results :
 -Hostname: `iotlab_upat_6`  
 -IP: `192.168.137.222`.
 -Connection attempt failed.

## 2. Enable SSH on the Raspberry Pi
```bash
sudo raspi-config
```
Then:
-Select Interface Options
-Select SSH
-Choose Enable
-Exit the tool

## 3.Verify ssh works 
On the Raspberry Pi:
```bash
systemctl status ssh
```
Result: **active (running)**

# Part-B. Remote-first workflow (SSH from laptop)
## 4. SSH from a team's member laptop
On the laptop :
```bash
ssh iotlab_upat_6@192.168.137.222
```
It required a password, which we gave the first time we connected by ssh.
## SSH key authentication.
Run the following:
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

## 5. Verification 
On the laptop run :
```bash
whoami
uptime
```
Results:
-whoami: `iotlab_upat_6`.

# Part-C. Baseline smoke test
## 6. Frequent root causes of failures and inconsistent results
On the laptop run :
```bush
uname -a
cat /etc/os-release
df -h
free -h
date
python3 --version
pip3 --version
```
Important Results : 
1. Correct system time and date
2. Python version downloaded on the laptop
3. Disc usage

# Part-D — Git and GitHub basics
## 7. Clone, add, commit, push 
Clone the repository:
```
git clone <repo-url>
cd <repo-folder>
```
In order to make the requested repository we used the code:
```
git status
git add README.md labs/
git commit -m "Lab01: initialize repository structure"
git push
```
## 8. Branching and conflict awareness
Create a branch:
```
git checkout -b lab01/<shortname>
```
Push the branch:
```
git push -u origin lab01/<shortname>
```

# Part-E — Reproducible Python environment on the Pi
## 9.
A Python virtual environment (`venv`) is an isolated environment that contains its own Python interpreter and installed packages. It ensures that the dependencies required for this project do not interfere with system-wide Python packages or other projects. Before installing dependencies or running the program, the virtual environment must be activated. This guarantees consistent package versions and improves reproducibility across different systems.

## 10. Create the venv 
From the labs/lab01 directory on the Raspberry Pi, run:
```bash
python3 -m venv venv
```
This way we created a folder named venv/ that contains the isolated environment.

## 11. Enable the venv
On the laptop we run :
```bush
source venv/bin/activate
```
After activation the terminal prompt showed (venv).

## 12. Validation 
Run the following :
```bush
which python
python --version
python -c "import sys; print(sys.executable)"
```
Results:
1.Python version: 3.13.5
2.The following python path :
/home/iotlab_upat_6/advanced-programming-techniques-lab/labs/lab01/venv/bin/python

## 13.Dependencies-Creation of requirments.txt
We used argparse which is part of Python’s standard library, so it does NOT need to be included in `requirements.txt`.
Then run the following in order to install dependencies into the venv :
```bush
pip install -r requirements.txt
```
Verify by running:
```bush
pip list
```
That shows all installed packages in the currently active environment, the venv in this case.

# Part-F — Build a mock event generator
## 14.What to build 
 A command-line tool named `event_generator.py` that simulates a wastebin device by writing JSON Lines (JSONL) event records to an output file.
 Saved at :
 File: labs/lab01/event_generator.py

 ## 15.Event types
 -Must support at least the following event types:. 
1.deposit: Something was thrown into the bin.
2.heartbeat: Shows that the software is running and is able to emit events.
 -Optional event types that were used:.
1.`--starting-total` : 
2.`--deposit-delta` 
3.`--verbose`
 -Added events :
1.`--lid_open`
2.`--lid_close`
3.`--maintance`
4.`--maintance_termination`
5.`--lid_clear`

## 16.CLI requirments
We used `argparse`, more details on step 13.

## 17. Output format - JSON Lines
The output file is an append-only event log.
Fields required in every record:.
 -event_time (ISO-8601 UTC, e.g. 2026-02-10T12:34:56.789Z)
 -ingest_time (ISO-8601 UTC)
 -device_id (string)
 -event_type (string)
 -seq (integer; starts at 1 and increments by 1)
 -run_id (string; unique per execution)

## 18. Strict error handling and exit codes
Required behavior:
1.Exit with code 2 for CLI/usage errors.
2.Exit with code 1 for runtime errors (for example, file I/O failures).
3.Print errors to stderr.
3.Reject invalid arguments:
 -count <= 0.
 -interval < 0.
 -unknown event_type.
4.If the program is interrupted (Ctrl-C), it must shut down gracefully.

## 19. The code 
Using the hints given we wrote the code that is saved as `event_generator.py`.
# Extended Wastebin Device Behavior
State Persistence and `--starting-total`
The program maintains persistent state by reading the existing JSONL log file.
## Default Behavior (No `--starting-total` Provided)
If `--starting-total` is not provided:

- The program reads the last `deposit_total` value from the existing output file.
- The new execution continues from that value.
- This allows the wastebin to "remember" its previous content.
## Override Behavior (`--starting-total` Provided)
If `--starting-total` is specified:

- The provided value overrides the stored value.
- The internal `deposit_total` is initialized with the user-defined value.
- Subsequent deposits increment from that value.
## Device State Model
The program simulates a stateful wastebin device.
It maintains internal state variables that affect event behavior:
- `lid_open` (boolean)
- `maintenance_mode` (boolean)
- `deposit_total` (integer)
Each new event updates these internal state variables accordingly.
The state determines whether a `deposit` event is accepted or rejected.
## Supported Event Types
## Core Events
- `deposit`
- `heartbeat`
## Extended Events
- `lid_open`
- `lid_close`
- `lid_clear`
- `maintenance`
- `maintenance_termination`
## Event Behavior Rules
1. `lid_clear`
Resets the wastebin.
- Sets `deposit_total = 0`
- Adds `"action": "cleared"` to the record
Example:
```bash
python event_generator.py --device-id wastebin-01 --event-type lid_clear --count 2 --interval 0.2 --out events.log --starting-total 6
```
Result:
deposit_total becomes 0 regardless of previous value.

2. . lid_open
Sets:
```
lid_open = True
```
Deposits are allowed only when the lid is open.

3.lid_close
Sets:
```
lid_open = False
```
Deposits are rejected when the lid is closed.
Rejected deposit example:
```JSONL
{
  "event_type": "deposit",
  "deposit_delta": 0,
  "deposit_total": 23,
  "status": "rejected",
  "reason": "lid_closed"
}
```

4.deposit

Accepted only if:
```
lid_open == True
```
```
maintenance_mode == False
```
If accepted:
 -`deposit_delta` is added
 -`deposit_total` increases
 -`"status"`: "accepted"

If rejected:
 -`deposit_delta` = 0
 -`deposit_total` remains unchanged
 -`"status"`: "rejected"
 -`"reason"` explains the cause

Example (accepted):
```JSONL
{
  "event_type": "deposit",
  "deposit_delta": 1,
  "deposit_total": 7,
  "starting_total": 6,
  "status": "accepted"
}
```
5. maintenance
Sets:
```
maintenance_mode = True
```
All deposits are rejected while in maintenance mode.
Rejected example:
```JSONL
{
  "event_type": "deposit",
  "status": "rejected",
  "reason": "maintenance_mode"
}
```
6. maintenance_termination
Sets:
```
maintenance_mode = False
```
Deposits are allowed again (if the lid is open).
## Verbose Mode
1. When `--verbose` is enabled:
 -The program prints progress information to stdout.
Progress messages are shown every 5 events.
Example:
```
generated seq=5 type=deposit out=events.log
generated seq=10 type=deposit out=events.log
```
# Example workflow:
 -`lid_clear` → resets total to 0
 -`lid_open` → deposits allowed
 -`deposit` → total increases
 -`lid_close` → deposits rejected
 -`maintenance` → deposits rejected
 -`maintenance_termination` → deposits allowed again (if lid open)

The system preserves state between executions unless overridden by `--starting-total`.


# Part-G — Mini-tests
## 20.Output example 
Test command used:
```bash
python event_generator.py --device-id wastebin-01 --event-type deposit --count 5 --interval 0 --out test_events.log
```
Result:
```json
{"event_time": "2026-02-28T21:35:11.458Z", "ingest_time": "2026-02-28T21:35:11.459Z", "device_id": "wastebin-01", "event_type": "deposit", "seq": 1, "run_id": "4fd96845-d1a2-4451-a0c4-29e6db8473e8", "deposit_delta": 1, "deposit_total": 1, "status": "accepted"}
```
## 21.Verify required behavior
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


# SECTION B - REPORT
# A.

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
## RQ51
- No Python version requirement.
- No mention of SSH needing to be enabled.
- No statement about required internet/network access.
- Hardware assumptions are not documented.
- Instructions given without exact commands.
- No clear use of `python3`.
- No explicit `pip install -r requirements.txt`.
- Commands are not fully copy-pasteable.
- Does not specify whether commands should run on:
  - The laptop, or
  - The Raspberry Pi.

 ## RQ52
 - Specified required hardware (Raspberry Pi)
 - Specified Python version (3.9+)
 - Stated that SSH, Git, and internet access are required
 - Clearly indicated whether each command must be executed on the laptop or on the Raspberry Pi.
 - Replaced unclear instructions such as “install dependencies” with complete, copy-pasteable commands.










