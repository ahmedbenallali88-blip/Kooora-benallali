# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from config import API_KEY, BASE_URL

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

headers = {
    "x-apisports-key": API_KEY
}

@app.get("/fixtures/today")
def get_today_fixtures():
    url = f"{BASE_URL}/fixtures?date=2025-10-07"
    response = requests.get(url, headers=headers)
    return response.json()

@app.get("/leagues")
def get_leagues():
    url = f"{BASE_URL}/leagues"
    response = requests.get(url, headers=headers)
    return response.json()

@app.get("/teams")
def get_teams():
    url = f"{BASE_URL}/teams?league=39&season=2025"
    response = requests.get(url, headers=headers)
    return response.json()
