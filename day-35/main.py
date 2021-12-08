import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "e402111f5dbfb9a650fec7fc4cc2f1e0"

account_sid = 'AC41e68ae177f91dce73a28a3756dde6b9'
auth_token = '8536ac1cace0a5a0e5b9a1b196fb5ea2'


# https://api.openweathermap.org/data/2.5/onecall?lat=44.426765&lon=26.102537&appid=e402111f5dbfb9a650fec7fc4cc2f1e0

weather_params = {
    "lat": 44.384361,
    "lon": 26.130505,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]


will_rain = False

for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today! ☂️",
        from_="+14432513193",
        to="+4012345"
    )
    print(message.status)


# path through json ["hourly"][0]["weather"][0]["id"]

# print(type(weather_data["hourly"][0]["weather"][0]))



