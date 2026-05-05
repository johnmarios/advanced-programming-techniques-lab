import json 
import os 

DATA_DIR = os.path.join(os.path.dirname(__file__), "data") 
EVENTS_FILE = os.path.join(DATA_DIR, "motion_events.jsonl") 
# dir where the motion event data is stored


def load_json(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


def load_events(filepath, limit=None, sensor_id=None):
    events = []

    if not os.path.exists(filepath):
        return events

    with open(filepath, "r") as f:

        for line in f: 
            line = line.strip()
        
            if not line:
                continue

            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue

            if sensor_id is not None and record.get("madeBySensor") != sensor_id:
                continue

            events.append(record)

    events.reverse()
    if limit is not None:
        events = events[:limit]
    return events

bin_model = api.model("Bin", {
    "id": fields.String(required=True, description="Bin unique identifier"),
    "name": fields.String(description="Human-readable name"),
    "location": fields.String(description="Deployment location"),
    "status": fields.String(description="Current status"),
})

event_model = api.model("Event", {
    "resultTime": fields.String(description="ISO timestamp of the event"),
    "madeBySensor": fields.String(description="Sensor ID that produced this event"),
    "hasSimpleResult": fields.String(description="Motion state (detected/clear)"),
    "pipeline_latency_ms": fields.Float(description="Pipeline latency in ms"),
})