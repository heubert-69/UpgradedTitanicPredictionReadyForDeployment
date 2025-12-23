from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load exported LightGBM model
model = joblib.load("lgb_model_titanic.pkl")

app = FastAPI(title="Titanic Survival Prediction API")

class Passenger(BaseModel):
    Pclass: int
    Sex: str
    Age: float
    SibSp: int
    Parch: int
    Fare: float

@app.post("/predict")
def predict_survival(passenger: Passenger):
    data = pd.DataFrame([passenger.dict()])
    
    # Encode Sex
    data['Sex'] = data['Sex'].map({'male':0, 'female':1})
    
    prediction = model.predict_proba(data)[:,1][0]
    return {"predicted_survival": round(float(prediction), 3)}
