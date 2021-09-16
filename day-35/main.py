import requests
from twilio.rest import Client
import os

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
OWN_API_KEY = os.environ.get("OWN_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_MESSAGING_SERVICE_SID = os.environ.get("TWILIO_MESSAGING_SERVICE_SID")
YOUR_PHONE_NUMBER = os.environ.get("YOUR_PHONE_NUMBER")
MY_LATITUDE = 50.447731
MY_LONGITUDE = 30.542721

weather_parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": OWN_API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OWN_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()["hourly"][7:19]
weather_codes = [_["weather"][0]["id"] for _ in weather_data]

will_rain = False

for _ in weather_codes:
    if int(_) < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="Remember to bring an umbrella!",
        messaging_service_sid=TWILIO_MESSAGING_SERVICE_SID,
        to=YOUR_PHONE_NUMBER
    )
    print(message.status)
