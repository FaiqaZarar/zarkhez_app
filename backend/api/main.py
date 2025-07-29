# backend/api/main.py

from fastapi import FastAPI
from backend.api import weather_routes

app = FastAPI()

app.include_router(weather_routes.router)

