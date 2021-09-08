import datetime as dt
import os
import pandas as pd
import requests as rq


GENDER = "male"
WEIGHT_KG = "65"
HEIGHT_CM = "170"
AGE = "25"

NX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

NX_APP_ID = os.environ.get("APP_ID")
NX_APP_KEY = os.environ.get("APP_KEY")
NX_TOKEN = os.environ.get("NX_TOKEN")

sheety_url = os.environ.get("SHEET_URL")

answer = "running for 80 seconds"

hd = {
    "x-app-id": NX_APP_ID,
    "x-app-key": NX_APP_KEY,
        
}

param = {
    "query": answer,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


request_nx = rq.post(url=NX_URL, json=param, headers=hd)
result = request_nx.json()

print(result)

today_date = dt.datetime.now().strftime("%d/%m/%Y")
time_now = dt.datetime.now().strftime("%H:%M:%S")

for exercise in result["exercises"]:

    duration = pd.to_datetime(exercise["duration_min"], unit='m').strftime("%H:%M:%S")
    
    workout = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": duration,
            "calories": exercise["nf_calories"],
        },
    }

    parameters = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {NX_TOKEN}",
    }

    request_sheet = rq.post(sheety_url, json=workout, headers=parameters)
    