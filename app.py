import os
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

PORT = int(os.getenv("PORT", 10000))

model = joblib.load("model.joblib")
label_map = {0: "human", 1: "AI"}

app = FastAPI()

class InputText(BaseModel):
    text: str
    instructions: str

app.add_middleware( CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True, 
                   allow_methods=["*"], 
                   allow_headers=["*"], )
@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/predict")
def predict(payload: InputText):
    df = pd.DataFrame([payload.dict()])
    pred = model.predict(df)[0]
    # Si le modèle a predict_proba (LogisticRegression oui)
    proba = None
    if hasattr(model, "predict_proba"):
        proba_vals = model.predict_proba(df)[0]
        proba = {
            "human": float(proba_vals[0]),
            "AI": float(proba_vals[1])
        }
    
    return {
        "prediction_raw": int(pred),
        "prediction_label": label_map[pred],
        "probabilities": proba
    }

    # return {"raw": int(pred), "label": label_map[pred]}

