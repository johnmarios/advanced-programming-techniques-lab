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
  As shown in lab01, in order to run the following code it's nesessary to connect to the raspberry pi 5 via ssh. Clear instructions can be found on lab01.
- Software:
  - The PIR sensor logic (`sampler.py`, `interpreter.py`) is reused from Lab 02 and placed inside `pirlib/`. 
  - Use a venv just like lab01 and lab02.
  - Make sure to inastall a `requirments.txt`.
## Part 1 — Install and start Mosquitto
On the laptop connected to the rpi run:
```
sudo apt-get update
sudo apt-get install -y mosquitto mosquitto-clients
```
After installing Mosquito run this command in order to make sure it works :
```
systemctl status mosquitto
```
This should give *Active : Active (running)* as a result.
## Part 2 — Explore MQTT from the terminal
1. Open 2 terminals (both connected to the rpi):
  1. Start a subscriber :
 ```
 mosquitto_sub -h localhost -t "test/hello"
```
  3. In the second terminal publish th following message :
```
mosquitto_pub -h localhost -t "test/hello" -m "world"
```
Correct output: "world" appears on the subscriber's terminal.

2. Topic hierarchy :
   1. On the subscriber's terminal write :
```
mosquitto_sub -h localhost -t "smartbin/pir-01/motion"
```
  2. On the publisher's terminal type:
```
mosquitto_pub -h localhost -t "smartbin/pir-01/motion" -m '{"state": "detected"}'
```
By this, it is clear that  MQTT does not care about the format, it just delivers bytes.

3. Wildcards
   With the subscriber still running, try these in separate terminals. On the first:
```
# Subscribe to ALL topics under smartbin/pir-01/
mosquitto_sub -h localhost -t "smartbin/pir-01/#"
```
On the second :
```
# Subscribe to motion events from ANY device
mosquitto_sub -h localhost -t "smartbin/+/motion"
```
In another terminal, publish to different topics and see which subscribers receive what:
```
mosquitto_pub -h localhost -t "smartbin/pir-01/motion" -m "detected"
mosquitto_pub -h localhost -t "smartbin/pir-01/status" -m "online"
mosquitto_pub -h localhost -t "smartbin/pir-02/motion" -m "detected"
mosquitto_pub -h localhost -t "smartbin/ultrasonic-01/fill" -m "72"
```
The results are given in the screenshots 

   
























