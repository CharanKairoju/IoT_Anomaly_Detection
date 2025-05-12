# 📡 IoT Anomaly Detection with Real-Time Visualization

![Anomaly Detection Plot](https://www.mdpi.com/sensors/sensors-23-02844/article_deploy/html/images/sensors-23-02844-g005.png)

*Sample output: Real-time temperature data with anomalies highlighted in red.*

## 🚀 Overview

This project simulates an IoT sensor that publishes temperature readings via MQTT. An anomaly detection system, using the Isolation Forest algorithm, processes these readings in real-time and visualizes anomalies on a live-updating graph.

## 🧰 Features

- **Simulated IoT Sensor**: Generates temperature data with occasional anomalies.
- **MQTT Communication**: Uses Mosquitto as the MQTT broker.
- **Anomaly Detection**: Implements Isolation Forest for unsupervised anomaly detection.
- **Real-Time Visualization**: Live plot of temperature readings with anomalies highlighted.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/CharanKairoju/iot-anomaly-detection.git
cd iot-anomaly-detection
