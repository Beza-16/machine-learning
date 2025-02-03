from fastapi import FastAPI
from pydantic import BaseModel

# Define the FlightData model
class FlightData(BaseModel):
    year: int
    month: int
    carrier: str
    carrier_name: str
    airport: str
    airport_name: str
    arr_flights: int
    arr_del15: int
    carrier_ct: float
    weather_ct: float
    nas_ct: float
    security_ct: float
    late_aircraft_ct: float
    arr_cancelled: int
    arr_diverted: int
    arr_delay: int
    carrier_delay: int
    weather_delay: int
    nas_delay: int
    security_delay: int
    late_aircraft_delay: int

# Initialize the FastAPI application
app = FastAPI()

@app.post("/predict_delay/")
async def predict_delay(flight_data: FlightData):
    # Prediction logic: if arr_delay is greater than 0, predict delay
    if flight_data.arr_delay > 0:
        prediction = "Yes"
    else:
        prediction = "No"

    # Return a message and delay prediction
    return {"message": "Prediction received!", "delay": prediction}
