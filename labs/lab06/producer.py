import paho.mqtt.client as mqtt
from pirlib import PirSampler, PirIntepreter
from pipeline_operations import *

BROKER="localhost"
TOPIC="pir"
PORT=1883


client = mqtt.Client("P1")
client.connect(BROKER,PORT,60)
client.loop_start()
sampler = PirSampler(pin=4)
interpreter = PirIntepreter(cooldown_s=5.0, min_high_s=0.5)

run_id = create_run_id() 
seq = 0
args,event_q,metrics =  setup()

while True:
    try:
        now = time.time()
        raw = sampler.read() # read the raw sensor value (e.g. 0 or 1 for PIR)
    except Exception as exc:
        print(f"[producer] sensor read error: {exc}", file=sys.stderr)
        continue

    for event in PirIntepreter.update(raw, now):
        seq += 1
        event_time = epoch_to_utc_iso(event["t"]) 

        record = create_event(
                event_time = event_time,
                device_id = args.device_id,
                wastebin_id = args.wastebin_id,
                environment_id = args.environment_id,
                event_type = "motion",
                motion_state = "detected",
                seq = seq,
                run_id = run_id,
                context_iri = args.context,
            )
        try:
            event_q.put_nowait(record) # puts without blocking until queue is full
            # i want the expection to be able to be raised to regulate the behavior 
            metrics["produced"] += 1
            current_q = event_q.qsize()
            metrics["max_queue"] = max(metrics["max_queue"], current_q)

            if args.verbose:
                # print: [producer] queued seq=1 state=detected event_time=2024-06-01T12:00:00.000Z
                print(f"[producer] queued seq={seq} state={record['motion_state']} event_time={event_time}",flush = True)


        except queue.Full:
            metrics["dropped"] += 1
            if args.verbose:
                # print: [producer] queue full, dropped seq=1
                print(f"[producer] queue full, dropped seq={seq}", file=sys.stderr)
    time.sleep(args.sample_interval)
    
client.loop_stop()