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
  - The PIR sensor logic (`sampler.py`, `interpreter.py`) is reused from Lab 02, as well as the pipeline (`run_pipeline.py`)  from lab03.
  - Use a venv just like the previous labs.
## Docker installation
- If the docher is installed run :
  ```bash
      docker --version
      docker compose version
- If it is not intalled run :
  ```bash
       curl -fsSL https://get.docker.com | sh
- By default every docker command would need sudo. To fix that, add your user to the docker group:
  ```bash
        sudo usermod -aG docker $USER

  

---
# SECTION B - REPORT
## RQ1
We used `python:3.11-slim`. Python 3.11 was chosen to match the version installed on the Raspberry Pi environment used in Labs 01–03, ensuring behavioural consistency.
## RQ2
- The Dockerfile creates 7 new layers on top of the base image layers inherited from `python:3.11-slim`.
- The following commands produces a new image layer
  - `RUN`, `COPY`, `ADD`, `ENV`, `WORKDIR` and the two `RUN` commands (`pip install` and `mkdir`) each produce a separate layer because they are separate instructions.
## RQ3
The disk usage is 232 MB and the content size is 50.7 MB.
## RQ4
By copying `requirements.txt` and running `pip install` first, the two layers are cached and reused on every build as long as `requirements.txt` has not changed. Only the final `COPY` commands get rebuilt on a code change.
If we reversed the order any edit to `run_pipeline.py` or `pirlib/` would invalidate the code layer, and Docker would have to re-run `pip install` from scratch on every single rebuild.
## RQ5
By default a Docker container runs in an isolated namespace and has no access to host hardware devices. The `--device /dev/gpiomem0:/dev/gpiomem` passes the GPIO memory device from the host into the container, making it visible at the specified path inside.
## RQ6
When the container exits, the writable layer that the json lines are written, is deleted and all data is lost.
## RQ7 
The pipeline behaved correctly inside Docker. Over a 60-second run it produced 12 events, consumed all 12, dropped none, and kept latency at 0 ms with a max queue depth of 1 — matching the Lab 03 normal-run results.
One notable difference is that the gpiozero printed a `PinFactoryFallback` warning on startup (`Falling back from lgpio: 'can not open gpiochip'`) and switched to an alternative pin factory. The pipeline still worked, but it shows that GPIO passthrough inside a container can be less straightforward than running directly on the host.
## RQ8
The memory limit had no effect on the Pi. The container continued running and used more than 32 MB without being killed.
## RQ9
Edge devices run multiple services on constrained hardware. Without limits, one misbehaving container (memory leak, infinite loop) can consume all RAM or CPU and crash the entire system. 
## RQ10
## RQ11
## RQ12
## RQ13
A virtual enviroment isolates Python packages. It does not isolate the Python interpreter version, system C libraries , the operating system, or processes. Other processes on the host can still see and interfere with it.
## RQ14
`rpi-lgpio` wraps `libgpiod`, a C shared library. If a teammate's Pi runs a different version of Raspberry Pi OS , the `libgpiod` version and `/dev/gpiochip*` naming differ. The same `requirements.txt` installs the same Python package but the code may still fail because the underlying system library is incompatible. A Docker image pins the OS userland as well, eliminating this discrepancy.
## RQ15
A virtual environment is a better choice than Docker when doing simple, local Python development where you only need to isolate dependencies and want a fast, lightweight setup without the overhead of containerization.
## RQ16
We would refer to use docker. The wastebin will run multiple services (sensor pipeline, MQTT broker, storage, dashboard) each with different dependencies. Docker Compose lets us define and start the full stack with one command, restart individual services independently, and hand the deployment to another team with no environment setup required





















