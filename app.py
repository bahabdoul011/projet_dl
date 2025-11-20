import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

PORT = int(os.getenv("PORT", 10000))

model = joblib.load("model.joblib")
label_map = {0: "human", 1: "AI"}

app = FastAPI()

class InputText(BaseModel):
    text: str
    instructions: str

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/predict")
def predict(payload: InputText):
    df = pd.DataFrame([payload.dict()])
    pred = model.predict(df)[0]
    return {"raw": int(pred), "label": label_map[pred]}
