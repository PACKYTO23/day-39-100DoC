from pprint import pprint
import requests

FLIGHT_DEALS_PRICES = "https://api.sheety.co/f34ae5bff87e0200b3b4b3eef4f978de/flightDeals/prices"


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=FLIGHT_DEALS_PRICES)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{FLIGHT_DEALS_PRICES}/{city['id']}",
                json=new_data
            )
            print(response.text)
