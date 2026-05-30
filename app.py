from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI(title="Predictive Maintenance API")

# Try to load the model if it exists
try:
    model = joblib.load('predictive_maintenance_rf.pkl')
except:
    model = None

@app.get("/")
def home():
    return {"status": "Online", "engine": "Predictive Maintenance API Ready"}