import smtplib
import time

import requests
from datetime import datetime

MY_LATITUDE = 51.507351
MY_LONGITUDE = -0.127758
MY_EMAIL = ""
MY_PASSWORD = ""


def is_iss_overhead():
    response = requests.get(url="https://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude - 5 <= MY_LATITUDE <= iss_latitude + 5 and \
            iss_longitude - 5 <= MY_LONGITUDE <= iss_longitude + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False


while True:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.ehlo()
            connect.starttls()
            connect.login(user=MY_EMAIL, password=MY_PASSWORD)
            connect.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look up to see an international space station!\n\nIndeed!"
            )
    time.sleep(60)
