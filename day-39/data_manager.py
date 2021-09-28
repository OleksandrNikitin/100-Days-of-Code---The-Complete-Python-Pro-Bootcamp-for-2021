import os
import requests

SHEETY_PRICES_ENDPOINT = (
    "https://api.sheety.co/c975e73939d842287a8da7b0acc52b07/flightDeals/prices"
)
HEADERS = {"Authorization": f"Bearer {os.environ.get('SHEETY_API_TOKEN')}"}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data
            )
            print(response.text)
