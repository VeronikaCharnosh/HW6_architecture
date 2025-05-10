from fastapi import FastAPI, Header, HTTPException
import requests
from pydantic import BaseModel

app = FastAPI()
app_name = "client_service:app"
APP_TOKEN = "SuperSecretToken"
BUSINESS_SERVICE_URL = "http://business_service:8000"

class ClientRequest(BaseModel):
    weight: float
    activity_level: str

@app.get("/")
def root():
    return {"message": "Client Service for interacting with water intake microservice"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/calculate")
def calculate_water(data: ClientRequest, authorization: str = Header(None)):
    if authorization != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Call Business Logic Service only
    process_response = requests.post(f"{BUSINESS_SERVICE_URL}/process", json=data.dict())
    processed_data = process_response.json()

    return processed_data
