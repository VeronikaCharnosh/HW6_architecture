from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()

class WaterRequest(BaseModel):
    weight: float
    activity_level: str  # 'low', 'medium', 'high'

@app.get("/")
def root():
    return {"message": "Business Logic Service for water intake calculation"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process")
def process(data: WaterRequest):
    time.sleep(1)  # simulate longer processing
    factor = {
        "low": 30,
        "medium": 35,
        "high": 40
    }.get(data.activity_level.lower(), 35)

    water_intake_ml = data.weight * factor
    water_intake_liters = round(water_intake_ml / 1000, 2)

    return {
        "weight": data.weight,
        "activity_level": data.activity_level,
        "recommended_water_liters": water_intake_liters
    }
