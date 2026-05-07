# Advanced Programming Techniques Lab

## Team Information

Members:

- Marios Ioannis Papadopoulos 1092834  
- Filippos Neofytos Theologos 1092633  
- Xristina Tzouda 1097346

---

# SECTION A - RUNBOOK

## Nesessary hardware and software from previous labs

- Hardware:
  - Raspberry Pi 5
  - HC-SR501 PIR motion sensor
  - Jumper wires(female to female)
- Wiring the sensor:
  Used the example given on lab02, made sure to connect the OUT on the same pin.
- Connection
  Due to bad connection, we weren't able to download `homeassistant` during lab time and by using ssh, so we worked on the raspberry.
- Software:
  - The PIR sensor logic (`sampler.py`, `interpreter.py`) is reused from Lab 02 and extended with taking in consideration the off/clear state and placed it inside `pirlib/`.
  - Installed Mosquitto brocker. Instructions givel on lab06
  - Installed Home Assistant and made our own dashboard.

## Part 1 — Set up Flask and Flask-RESTx

1. Write on requirments.txt:

```
flask
flask-restx
```

2. Install:

```
pip install flask flask-restx
```

3. By writing the code given on lab's website we made sure that API works.

# SECTION B - REPORT

## RQ2
Event-listing endpoints use GET because they only retrieve data and do not change anything on the server. GET is safe and idempotent.
## RQ3
The “mark as emptied” endpoint uses POST because it performs an action that may create side effects or new records. POST is suitable for non-idempotent operations, unlike PUT.
## RQ7
`api.model` in Flask-RESTx defines the structure of request and response data. These models are automatically used to generate the Swagger UI documentation.
When we add a new field to a model, the Swagger UI updates automatically to show the new field in the endpoint documentation, including type and description.
## RQ9
`POST /mqtt/publish` receives a topic and message from an HTTP request and publishes the message to the MQTT broker.
## RQ10
The HTTP request is sent to the API → the API publishes the message to the MQTT broker → subscribers receive the message → the consumer stores it in the JSONL file.
## RQ11
`GET /mqtt/topics` returns the MQTT topics the API has received or subscribed to. The subscription to `smartbin/#` is needed so the API can listen to all topics under *smartbin*.
## RQ12
Combining database storage and MQTT publishing in one endpoint ensures an event is permanently saved and immediately shared with  any other systems in real time.
## RQ13
AsyncAPI documents event-driven (MQTT) communication, while OpenAPI documents REST endpoints. We need both because a Smart Wastebin project like ours uses REST for control and actions, while using  MQTT for real-time events.
## RQ19
We would give them the Swagger UI (OpenAPI) for REST endpoints and the AsyncAPI spec for MQTT events. Swagger shows how to read and update bin data and report when bins are full, while AsyncAPI shows real-time bin status updates via MQTT topics.
## RQ20
The system needs REST for actions like reporting bins and fetching data and MQTT for real-time updates, like sensor events.If we only used REST, there would be no real-time updates and If we used MQTT alone , users couldn’t easily request or manage data on demand.