## RQ1
A PIR sensor is **passive** and **no-contact**.  
It does not emit energy; it only detects changes in infrared heat from movement.

## RQ2
The output is **digital** (2 states):
- `LOW` → no motion
- `HIGH` → motion detected (~3.3V logic)

## RQ3
If `TIME = 300s`, software may wrongly assume there is **continuous motion** for 5 minutes.  
In reality, one trigger can keep the signal `HIGH` for that whole time window.

## RQ4
Warm-up matters because the first **30–60 seconds** can be unstable/noisy.  
If you log immediately, you may record false motion events.

## RQ5
By mixing BCM and BOARD numbering, there will be bugs since the pin referenced in the code will not match the physical one.

For example:

- **BCM GPIO17** = **BOARD physical pin 11**
- **BOARD physical pin 17** = **3V3 power**

## RQ6:
|Sensor pin |	Pi pin (physical) |	Pi name (BCM) |	Why      |
|-----------|---------------------|---------------|----------|
|VCC	    |	                 2|	            5V|power     |
|GND	    |	                 6|	           GND|reference |
|OUT	    |	                11|	        GPIO17|input signal|

## RQ7:
We selected GPIO17(BCM) since it has no special function, thus avoiding future conflicts.

## RQ8:
![alt text](RQ8.png)

## RQ9:
Approximately  3 seconds

## RQ10:
Approximately  5 minutes (300 seconds)

## RQ11:
Low sensitivity: Approximately 3 meters
High sensitivity: Approximately 7 meters

## RQ12


## RQ13


