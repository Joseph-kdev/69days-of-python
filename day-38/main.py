import requests
from datetime import datetime
import os

APP_ID =os.environ["NT_APP_ID"]
BEARER_TOKEN = os.environ["TOKEN"]
API_KEY =os.environ["NT_API_KEY"]
GENDER = "male"
WEIGHT_KG = "66"
HEIGHT_CM = "183"
AGE = "23"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

exercise = input("Tell me which exercises you did: ")
nlp_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nlp_exercise_endpoint, headers=headers, json=parameters)
response.raise_for_status()
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
bearer_header = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    sheet_response = requests.post(sheet_endpoint, json=sheet_input, headers= bearer_header)
    
    print(sheet_response.text)

