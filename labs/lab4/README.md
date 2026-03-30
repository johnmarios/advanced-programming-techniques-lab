# Advanced Programming Techniques Lab
## Team Information
Members: 
- Marios Ioannis Papadopoulos 1092834
- Filippos Theologos 1092633
- Xristina Tzouda 1097346
---
# SECTION A - RUNBOOK 


---
# SECTION B - REPORT
## RQ1
We used `python:3.11-slim`. Python 3.11 was chosen to match the version installed on the Raspberry Pi environment used in Labs 01–03, ensuring behavioural consistency.
## RQ2
- The Dockerfile creates 7 new layers on top of the base image layers inherited from `python:3.11-slim`.
- The following commands produces a new image layer
  - `RUN`, `COPY`, `ADD`, `ENV`, `WORKDIR` and the two `RUN` instructions (`pip install` and `mkdir`) each produce a separate layer because they are separate instructions.

