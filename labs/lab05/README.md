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

# SECTION B - REPORT
## RQ1
We used three vocabularies across our models:
- SOSA/SSN (http://www.w3.org/ns/sosa/) — purpose-built for sensors, observations, and actuators. It has exact concepts like Sensor, Observation, ObservableProperty, and resultTime that map directly to our PIR sensor setup. Alternatives like SAREF are also suitable but less widely supported by open tools.
- schema.org (https://schema.org/) — for general metadata: name, description, manufacturer, Place. It's the most widely understood vocabulary on the web, making our models more accessible.
- BOT (https://w3id.org/bot#) — the Building Topology Ontology, designed specifically for describing spatial relationships between rooms, floors, and buildings. Used in environment.jsonld.
- Custom pipeline: namespace — for pipeline-internal fields (seq, run_id, pipeline_latency_ms) that no standard vocabulary covers.














