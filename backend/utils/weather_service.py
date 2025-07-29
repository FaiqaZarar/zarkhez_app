import httpx

API_KEY = "00c2e68cb6837d00431061f397f79490"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

async def get_weather_by_city(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(BASE_URL, params=params)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"error": str(e)}
