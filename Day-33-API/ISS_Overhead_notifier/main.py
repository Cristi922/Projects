import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "test"

MY_LAT = 45.16923 # Your Tulcea latitude
MY_LONG = 28.81138 # Your Tulcea longitude


# MY_LAT = 44.384227 # Your Bucharest latitude
# MY_LONG = 26.130623 # Your Bucharest longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG+5 <= iss_longitude <= MY_LONG+5:
        return True



#Your position is within +5 or -5 degrees of the ISS position.


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 3
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 3

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
print("running")
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="test@test.com",
            msg="Subject:Look Up\n\n The ISS is above you in the sky"
        )

