import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 183.00
AGE = 28

APP_ID = "dd64ff19"
API_KEY = "0a9c868d30c54440cea7ec7234c83444"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/ced74d00bf9adf651c614dbe00840845/workoutTracking/workouts/"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

#===================== Basic Authentification =====================

# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     auth=(
#         "Cristi",
#         "123asd123ASD"
#     )
# )

#===================== Bearer Token Authentication =====================

bearer_headers = {
    "Authorization": "Bearer kegnwjjlkegnjl2w3jt2opl;tmqwmgjpoqwjp"
}

sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)



