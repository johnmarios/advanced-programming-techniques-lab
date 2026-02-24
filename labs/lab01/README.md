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
