import time
import random
import paho.mqtt.client as mqtt
import json

client = mqtt.Client()
client.connect("localhost")

while True:
    temp = round(random.uniform(20, 25), 2)
    if random.random() < 0.1:
        temp += random.uniform(10, 20)  # Inject anomaly

    payload = {
        "device_id": "sensor_1",
        "temperature": temp,
        "timestamp": time.time()
    }

    client.publish("iot/temp", json.dumps(payload))
    print("Sent:", payload)
    time.sleep(1)
