from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import create_db, get_session
from models import SensorReading

app = FastAPI()

@app.on_event("startup")
def startup():
    create_db()

# Arduino/ESP32 posts data here
@app.post("/sensor")
def receive_data(reading: SensorReading, session: Session = Depends(get_session)):
    session.add(reading)
    session.commit()
    session.refresh(reading)
    return {"status": "saved", "id": reading.id}

# Get all readings
@app.get("/readings")
def get_readings(session: Session = Depends(get_session)):
    readings = session.exec(select(SensorReading).limit(100)).all()
    return readings

# Test route
@app.get("/")
def home():
    return {"message": "Sanitation Backend is running!"}