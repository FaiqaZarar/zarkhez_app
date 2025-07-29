from fastapi import APIRouter, Query
import requests
import os
from dotenv import load_dotenv

router = APIRouter()
load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def generate_advice(weather_data):
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    condition = weather_data['weather'][0]['main'].lower()

    advice = []

    if temp > 35:
        advice.append("Very hot day. Irrigate early morning or late evening.")
    elif temp < 15:
        advice.append("Cold weather. Monitor crops for frost damage.")

    if humidity > 70:
        advice.append("High humidity. Increased risk of fungal disease.")
    elif humidity < 30:
        advice.append("Low humidity. Ensure sufficient irrigation.")

    if "rain" in condition:
        advice.append("Rain expected. Delay irrigation and fertilization.")
    elif "clear" in condition:
        advice.append("Clear skies. Normal farming operations are good to go.")

    return " ".join(advice)


@router.get("/weather")
def get_weather(
    lat: float = Query(default=None),
    lon: float = Query(default=None),
    city: str = Query(default=None)
):
    params = {
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    if city:
        params["q"] = city
    elif lat and lon:
        params["lat"] = lat
        params["lon"] = lon
    else:
        return {"error": "Please provide either city name or lat & lon."}

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return {"error": "Failed to fetch weather data."}

    data = response.json()
    advice = generate_advice(data)

    return {
        "location": data.get("name"),
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"].capitalize(),
        "humidity": data["main"]["humidity"],
        "advice": advice
    }
