# 🛠️ End-to-End Predictive Maintenance API

A production-ready, containerized Machine Learning pipeline that predicts industrial equipment failure based on real-time sensor metrics. This project transitions from a prototype Jupyter Notebook to a cloud-deployed REST API capable of serving real-time predictions.

🚀 **Live Interactive API Testing Dashboard:** (https://anuragn2107-predictive-maintenance-api.hf.space/docs)  

---

## 📌 Project Overview
Industrial downtime costs manufacturing industries millions annually. This project develops a machine learning application that ingests real-time telemetry data (temperatures, speed, torque, wear) and instantaneously evaluates whether a machine requires immediate maintenance.

### Key Features:
* **Machine Learning Model:** Trained a robust **Random Forest Classifier** to analyze complex correlations between operating stress and device breakdowns.
* **REST API:** Built a high-performance backend application using **FastAPI** to manage requests and enforce runtime data validation using **Pydantic**.
* **Containerization:** Bundled all source code, dependencies, and model binaries using **Docker** for local and cloud environmental parity.
* **Cloud Deployment:** Hosted the container natively on **Hugging Face Spaces** to maintain 24/7 global availability.

---

## 📂 Repository Structure
```text
├── .gitignore                          # Prevents tracking system caches and virtual environments
├── Dockerfile                          # Build blueprint for the Docker container image
├── README.md                           # Project documentation (This file)
├── app.py                              # FastAPI backend application script
├── predictive_maintenance_rf.pkl       # Serialized (trained) Random Forest model binary
├── predictive_maintenance_training.ipynb # Google Colab notebook demonstrating EDA and modeling
└── requirements.txt                    # Project library dependencies

---

## 📊 Core Data Architecture

The API accepts structured telemetry payloads matching the following operational parameters:

| Sensor Attribute | Type | Example Value | Description |
| :--- | :--- | :--- | :--- |
| `air_temp` | Float | `300.0` | Ambient temperature around the machine |
| `process_temp` | Float | `310.0` | Internal engine operational temperature |
| `rotational_speed` | Float | `2800.0` | Engine speed in Rotations Per Minute (RPM) |
| `torque` | Float | `65.0` | Rotational mechanical torque load |
| `tool_wear` | Float | `240.0` | Wear and tear status time on cutting tools |
| `temp_diff` | Float | `10.0` | Calculated difference between process and air temp |
| `power_index` | Float | `182000.0` | Aggregated mechanical power requirement metric |
