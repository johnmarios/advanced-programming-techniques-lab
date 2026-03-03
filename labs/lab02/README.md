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