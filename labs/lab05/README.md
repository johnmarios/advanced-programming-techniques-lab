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
- Added entity normalization function (`normalize_entity_id()`) to ensure URN format
- Updated `create_event()` to accept `context_iri`, `wastebin_id`, and `environment_id` parameters
- Every output record now includes:
  - `@context`: reference to external JSON-LD context file (`models/context.jsonld`)
  - `@type`: semantic type (`sosa:Observation`)
  - Entity IRIs: device_id, wastebin_id, environment_id as proper URNs (urn:dev:team-06:*)
  - Pipeline metadata: run_id, sequence number, ingest_time, latency_ms

---

## Data Model Overview

The PIR sensor deployment is described using a **domain model** that defines relationships between four key entities:

```
Entity → Relationships → Context

PirSensor (¶1) ──deployedIn──→ Wastebin (¶2)
   │                                │
   ├──environment───→ Environment (¶3)
   │
   └──madeBySensor──→ Observation Records
                            │
                            ├──observedProperty: Motion
                            ├──resultTime: timestamp
                            └──contextualReferences: Wastebin, Environment
```

### Entities and Properties

**1. PirSensor (ck801:PirSensor)**
- **ID**: `urn:dev:team-06:pir-01`
- **Type**: SOSA Sensor subclass
- **Key Properties**:
  - `sensingPrinciple`: passive infrared
  - `range`: 2–7 meters
  - `cooldown`: 5 seconds (detection hold-off)
  - `operatingTemperature`: −15 to 70°C
  - `pins`: GPIO.17 (wired connection)
- **Relationships**: deployed in wastebin-01, located in environment-01

**2. Wastebin (ck801:Wastebin)**
- **ID**: `urn:dev:team-06:wastebin-01`
- **Type**: ck801:Wastebin (schema.org:Product subclass)
- **Key Properties**:
  - `capacityLiters`: 0.5 L
  - `material`: plastic
  - `color`: grey
  - `wasteType`: paper
  - `collectionZone`: Zone A
- **Relationships**: hosts pir-01, located in environment-01

**3. Environment (bot:Space)**
- **ID**: `urn:dev:team-06:environment-01`
- **Type**: Building Topology Ontology Space
- **Key Properties**:
  - `environmentType`: indoor
  - `zone`: Zone A
  - `traffic`: high (busy area)
  - `location`: Kypes classroom (23.7283°N, 37.9838°E)
- **Relationships**: hosts pir-01, contains wastebin-01

**4. Motion (ck801:Motion)**
- **Type**: Observable Property
- **Values**: `detected` | `not-detected`
- **Observed By**: PirSensor
- **Recorded In**: Each sosa:Observation

### Observation Records Structure

Every motion detection event is captured as an `sosa:Observation` with semantic markup:

```json
{
  "@context": "models/context.jsonld",
  "@type": "sosa:Observation",
  "event_time": "2026-04-06T14:30:45.123Z",
  "device_id": "urn:dev:team-06:pir-01",
  "wastebin_id": "urn:dev:team-06:wastebin-01",
  "environment_id": "urn:dev:team-06:environment-01",
  "event_type": "ck801:Motion",
  "motion_state": "detected",
  "seq": 1,
  "run_id": "a1b2c3d4-e5f6-...",
  "ingest_time": "2026-04-06T14:30:45.150Z",
  "pipeline_latency_ms": 27.5
}
```

**Key Fields Explained:**
- `@context`: Points to `models/context.jsonld`, which maps field names to standard ontology terms (sosa:resultTime, sosa:madeBySensor, ck801:Motion, etc.)
- `@type`: Declares this record as a SOSA Observation (semantic self-description)
- Entity IRIs: device_id, wastebin_id, environment_id are URNs, enabling linking to their JSON-LD definitions
- Pipeline metadata: seq, run_id, ingest_time, latency_ms track event flow and performance

### Running the Pipeline with Models

Execute the pipeline with explicit entity references:

```bash
python labs/lab05/run_pipeline.py \
  --device-id urn:dev:team-06:pir-01 \
  --wastebin-id urn:dev:team-06:wastebin-01 \
  --environment-id urn:dev:team-06:environment-01 \
  --context models/context.jsonld \
  --pin 17 \
  --duration 60.0 \
  --out events.jsonl
```

Each line in `events.jsonl` will now be **self-describing**: a reader can:
1. See it's a SOSA Observation (via `@type`)
2. Look up term definitions in the referenced `@context`
3. Follow entity IRIs to `models/sensor.jsonld`, `models/wastebin.jsonld`, `models/environment.jsonld`
4. Understand the complete deployment context without external documentation






  



# SECTION B - REPORT
## RQ1
We used three vocabularies across our models:
- SOSA/SSN (http://www.w3.org/ns/sosa/) — purpose-built for sensors, observations, and actuators. It has exact concepts like Sensor, Observation, ObservableProperty, and resultTime that map directly to our PIR sensor setup. Alternatives like SAREF are also suitable but less widely supported by open tools.
- schema.org (https://schema.org/) — for general metadata: name, description, manufacturer, Place. It's the most widely understood vocabulary on the web, making our models more accessible.
- BOT (https://w3id.org/bot#) — the Building Topology Ontology, designed specifically for describing spatial relationships between rooms, floors, and buildings. Used in environment.jsonld.
- Custom pipeline: namespace — for pipeline-internal fields (seq, run_id, pipeline_latency_ms) that no standard vocabulary covers.














