# 🛠️ End-to-End Predictive Maintenance API

A production-ready, containerized Machine Learning pipeline that predicts industrial equipment failure based on real-time sensor metrics. This project transitions from a prototype Jupyter Notebook to a cloud-deployed REST API capable of serving real-time predictions.

🚀 **Live Interactive API Testing Dashboard:** [https://anuragn2107-predictive-maintenance-api.hf.space/docs](https://anuragn2107-predictive-maintenance-api.hf.space/docs)  

---

## 📌 Project Overview
Industrial downtime costs manufacturing industries millions annually. This project develops a machine learning application that ingests real-time telemetry data (temperatures, speed, torque, wear) and instantaneously evaluates whether a machine requires immediate maintenance.

### Key Features:
* **Machine Learning Model:** Trained a robust **Random Forest Classifier** to analyze complex correlations between operating stress and device breakdowns.
* **REST API:** Built a high-performance backend application using **FastAPI** to manage requests and enforce runtime data validation using **Pydantic**.
* **Containerization:** Bundled all source code, dependencies, and model binaries using **Docker** for local and cloud environmental parity.
* **Cloud Deployment:** Hosted the container natively on **Hugging Face Spaces** to maintain 24/7 global availability.

---

## 🛠️ Tools & Technologies Used

| Category | Technology | Description |
| :--- | :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) | Core programming language for data pipeline and backend API development. |
| **Machine Learning** | ![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) | Used to implement train-test splits, feature scaling, and the Random Forest model. |
| **Notebook Environment** | ![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white) | Used for exploratory data analysis (EDA), iterative modeling, and initial validation. |
| **API Framework** | ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) | High-performance, production-ready web framework with built-in OpenAPI (/docs) documentation. |
| **Data Validation** | ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white) | Enforces strict runtime type-checking and telemetry schema structures for incoming data. |
| **Containerization** | ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) | Wraps the code, runtime, libraries, and model binaries into an immutable container image. |
| **Cloud Hosting** | ![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow?style=for-the-badge) | Cloud hosting infrastructure used to serve the containerized API production endpoints globally. |

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
