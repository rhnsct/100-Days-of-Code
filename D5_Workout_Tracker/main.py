import requests as rq
import os


GENDER = "male"
WEIGHT_KG = "65"
HEIGHT_CM = "170"
AGE = "25"

URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

nx_app_id = os.environ.get("APP_ID")
nx_app_key = os.environ.get("APP_KEY")

answer = "2 squats"

hd = {
    "x-app-id": nx_app_id,
    "x-app-key": nx_app_key,
    
}

param = {
    "query": answer,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


request = rq.post(url=URL, json=param, headers=hd)
request.raise_for_status()
result = request.json()

print(result)