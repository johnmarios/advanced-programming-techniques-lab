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
  Use the example given on lab02, made sure to connect the OUT on the same pin.
- Connection
  Due to bad connection, we weren't able to download `homeassistant` during lab time and by using ssh, so we worked on the raspberry.
- Software:
  - The PIR sensor logic (`sampler.py`, `interpreter.py`) is reused from Lab 02 and placed inside `pirlib/`. 
  - Use a venv just like lab01 and lab02.
  - Make sure to inastall a `requirments.txt`.
  - Install Mosquitto brocker. Instructions givel on lab06
## Part 1 — Run Home Assistant in Docker
1. Create a directory for Home Assistant configuration:
```
mkdir -p ~/homeassistant/config
```
2. Run home assistant:
```
docker run -d \
  --name homeassistant \
  --restart unless-stopped \
  -v ~/homeassistant/config:/config \
  -v /run/dbus:/run/dbus:ro \
  --network host \
  ghcr.io/home-assistant/home-assistant:stable
```
3. When it starts run :
```
docker logs -f homeassistant
```
4. We run it directly on the raspberry so we used the following line on the browser `http://localhost:8123`.
## Part 2 — Connect Home Assistant to your MQTT broker
- Create the Mosquitto configuration file:
```
sudo nano /etc/mosquitto/conf.d/default.conf
```
- Add:
```
listener 1883
allow_anonymous true
```
- Restart Mosquitto:
```
sudo systemctl restart mosquitto
```
- Then we followed the instructions given on the lab course in order to add the MQTT on home assistant.
## Verifying the connection
- Follow this path on the home assistant :
  - Settings → Devices & Services → MQTT
- Subscribe to # (meaning all topics)
- Publish the:
  - Topic : `test/ha`
  - Payload: **hello from Home Assistant**
- The payload should be visible
- Publish from the terminal:
  - `mosquitto_pub -h localhost -t "test/from-terminal" -m "hello from terminal"`
- It showed up in the Home Assistant MQTT listener, so the bridge is working.
## Part 3 — Understand MQTT Discovery
## Create motion sensor entity:
1. Publish a configuration message to `homeassistant/binary_sensor/pir_01_motion/config`
2. Write the following payload:
```
{
  "name": "PIR Motion Sensor",
  "state_topic": "smartbin/bin-01/pir-01/motion",
  "payload_on": "detected",
  "payload_off": "clear",
  "device_class": "motion",
  "unique_id": "pir_01_motion",
  "device": {
    "identifiers": ["pir-01"],
    "name": "PIR Sensor 01",
    "model": "HC-SR501",
    "manufacturer": "Generic"
  }
}
```
This tells the home assistant to create a binary sensor, something that is On or OFF. It also says that the if the topic receives "detected", the entity is ON and if  it receives "clear", it is OFF. 
Try it from terminal:
```
mosquitto_pub -h localhost -t "homeassistant/binary_sensor/pir_01_motion/config" -r -m '{
  "name": "PIR Motion Sensor",
  "state_topic": "smartbin/bin-01/pir-01/motion",
  "payload_on": "detected",
  "payload_off": "clear",
  "device_class": "motion",
  "unique_id": "pir_01_motion",
  "device": {
    "identifiers": ["pir-01"],
    "name": "PIR Sensor 01",
    "model": "HC-SR501",
    "manufacturer": "Generic"
  }
}'
```


























