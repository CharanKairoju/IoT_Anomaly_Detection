import json
import matplotlib.pyplot as plt # type: ignore
from matplotlib.animation import FuncAnimation # type: ignore
import paho.mqtt.client as mqtt
from sklearn.ensemble import IsolationForest # type: ignore
import numpy as np # type: ignore

temps = []
anomalies = []

model = IsolationForest(contamination=0.1)

def detect_anomaly():
    if len(temps) >= 20:
        X = np.array(temps[-20:]).reshape(-1, 1)
        preds = model.fit_predict(X)
        for i in range(-20, 0):
            if preds[i + 20] == -1:
                anomalies.append(i + len(temps))

def on_message(client, userdata, msg):
    global temps
    data = json.loads(msg.payload.decode())
    temp = data["temperature"]
    temps.append(temp)
    detect_anomaly()

client = mqtt.Client()
client.connect("localhost")
client.subscribe("iot/temp")
client.on_message = on_message
client.loop_start()

# Plotting
fig, ax = plt.subplots()
def animate(i):
    ax.clear()
    ax.plot(temps, label="Temperature")
    ax.scatter(anomalies, [temps[i] for i in anomalies], color="red", label="Anomaly")
    ax.set_title("Real-Time Temperature Monitoring")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()

ani = FuncAnimation(fig, animate, interval=1000)
plt.show()
