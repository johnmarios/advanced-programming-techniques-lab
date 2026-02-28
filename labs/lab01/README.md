# Advanced Programming Techniques Lab

## Team Information
Repository created by Giannis Marios Papadopoulos.  
The rest of the team joined as invited collaborators.

Members: 
Marios Ioannis Papadopoulos 1092834
Filippos Theologos 1092633
Xristina Tzouda 1097346

---


# A.

## RQ1
Hostname: `iotlab_upat_6`  
IP: `192.168.137.222`

## RQ2
Connection attempt failed.

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
Answered in RQ18.

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
We used `click`.  
If we had used `argparse`, it would not need to be included in `requirements.txt` because it is part of Python’s standard library, while `click` must be included since it is a third-party package.

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

## CLI INPUT

Generate 5 deposit events:
```bash
python event_generator.py \
  --device-id wastebin-01 \
  --event-type deposit \
  --count 5 \
  --interval 0.2 \
  --out events.log
```

Generate 3 heartbeat events:
```bash
python event_generator.py \
  --device-id wastebin-01 \
  --event-type heartbeat \
  --count 3 \
  --interval 0.5 \
  --out events.log
```



## F.1 / F.2

## RQ31
Real systems begin with noisy, low-level sensor signals.We started by creating this mock event generator so we can focus on:
- CLI design  
- Validation and error handling  
- Append-only logging  
- Record sequencing  
- Timestamping  
- Clean shutdown behavior  

## RQ32
- Strict CLI validation (`--count > 0`, `--interval >= 0`, valid `--event-type`)
- Correct JSON Lines formatting (one valid JSON object per line)
- Append-only file behavior (`"a"` mode)
- Required field presence (`event_time`, `ingest_time`, `device_id`, `seq`, `run_id`)
- ISO-8601 UTC timestamp formatting (`...Z`)
- Sequence correctness (`seq` increments by exactly 1)
- Monotonic `deposit_total` logic
- Clean multi-run appends to the same file

## RQ33
- `deposit` answers: “Did the wastebin just get used?”
- `heartbeat` answers: “Is the wastebin online and functioning?”
Separating activity from liveness improves system observability and allows monitoring systems to distinguish between inactivity and failure.

## RQ34
If `heartbeat` events are missing, a monitoring system could incorrectly assume the device is offline, even if it is simply idle and functioning correctly.

## F.3

## RQ35
- `--starting-total` (default 0): Allows simulation of a device with pre-existing deposit state, ensuring `deposit_total` behaves as a cumulative counter.
- `--verbose`: Enables periodic operational output (every 5 records) without contaminating the JSONL event log.

## RQ36
Failing early prevents:
- Corrupt or logically invalid event logs  
- Undefined runtime behavior   

## F.4 / F.5 

## RQ37
JSON Lines is a good fit because:
- Each record can be parsed independently.
- New records can be appended safely without rewriting the file.
- Large logs can be streamed line-by-line.

## RQ38
`seq` guarantees deterministic ordering within a run.  
Timestamps provide real-world timing context.  
Together, they enable correctness validation and traceability.

## RQ39
This makes sure the counter reflects consistent state progression and prevents logical corruption.

## RQ40
Verifying that `deposit_total` increases exactly by 1 per record is hardest manually, especially in long append-onlylogs because it requires checking both monotonicity and step size consistency.

## F.6

## RQ41
- Break JSON parsing  
- Corrupt structured logs  
- Violate the “one JSON object per line” requirement  

## RQ42
- Confirm progress  
- Debug runtime issues  
- Diagnose file I/O failures  
- Observe interrupt behavior  

## F.7 / F.8 

## RQ43
This distinction allows our system to differentiate between incorrect user input and system-level failures.

## RQ44
Automated systems can:
- Detect failure types programmatically  
- Retry on runtime errors  
- Fail fast on usage errors  
- Trigger alerts conditionally  

## RQ45
Without handling:
- The file may contain incomplete writes  
- Buffered data may not flush  
- The user may not know how many records were successfully written  
- Debugging becomes more difficult  

## RQ51 
- No statement about required internet access or needing hotspot access.
- No mention of SSH needing to be enabled.
- No mention or help if an error occurs.
- No Python version requirement.
- Instructions like “install dependencies” without exact commands.
- No clear use of `python3`.
- Commands are not fully copy-pasteable.
- Does not specify whether commands should run on the laptop or the Raspberry Pi.
- No instruction to activate the venv before installing or running.

## RQ52



