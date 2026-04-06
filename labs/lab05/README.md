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
  - Create a docker like it is shown on lab04.
## Create the model files 
Using the instructions given on the lab's website we werw able to write the JSONLD documents in order to make the result data readable by everyone, just by following the links
## Create the ontopology documentation 
The Ontopoly auto-builds editing forms from your ontology. Define `Wastebin` properties once, get the right UI automatically. Like the JSON-LD `@context`.
## Update the Pipeline
- Modify `run_pipeline.py` to include the @context reference and entity links in every output record.
- Add the following on the file :
  ```

Then run :
```

```
The output :









  



# SECTION B - REPORT
## RQ1
We used three vocabularies across our models:
- SOSA/SSN (http://www.w3.org/ns/sosa/) — purpose-built for sensors, observations, and actuators. It has exact concepts like Sensor, Observation, ObservableProperty, and resultTime that map directly to our PIR sensor setup. Alternatives like SAREF are also suitable but less widely supported by open tools.
- schema.org (https://schema.org/) — for general metadata: name, description, manufacturer, Place. It's the most widely understood vocabulary on the web, making our models more accessible.
- BOT (https://w3id.org/bot#) — the Building Topology Ontology, designed specifically for describing spatial relationships between rooms, floors, and buildings. Used in environment.jsonld.
- Custom pipeline: namespace — for pipeline-internal fields (seq, run_id, pipeline_latency_ms) that no standard vocabulary covers.














