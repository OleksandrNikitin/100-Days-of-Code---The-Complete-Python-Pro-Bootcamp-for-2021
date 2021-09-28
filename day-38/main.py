import os
from datetime import datetime

import requests

GENDER: str = "male"
WEIGHT_KG: float = 72.3
HEIGHT_CM: float = 185.1
AGE: int = 25

EXERCISE_API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
EXERCISE_APP_ID = os.environ.get("EXERCISE_APP_ID")
EXERCISE_API_KEY = os.environ.get("EXERCISE_API_KEY")

SHEETY_API_URL = "https://api.sheety.co/c975e73939d842287a8da7b0acc52b07/day38/workouts"
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")

exercise_headers = {
    "x-app-id": EXERCISE_APP_ID,
    "x-app-key": EXERCISE_API_KEY,
    "x-remote-user-id": "0",
}

exercise_body = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

exercise_response = requests.post(
    url=EXERCISE_API_URL, json=exercise_body, headers=exercise_headers
)
exercise_response.raise_for_status()
exercise_data = exercise_response.json()["exercises"]

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}",
}

sheety_body = {
    "workout": {
        "date": datetime.today().strftime("%d/%m/%Y"),
        "time": datetime.today().strftime("%H:%M:%S"),
        "exercise": exercise_data[0]["name"].title(),
        "duration": exercise_data[0]["duration_min"],
        "calories": exercise_data[0]["nf_calories"],
    }
}

sheety_response = requests.post(
    url=SHEETY_API_URL, json=sheety_body, headers=sheety_headers
)
sheety_response.raise_for_status()
