import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "qgoZd7cPefsxl-5kktqg3tUz3R09sYox"
TEQUILA_SEARCH_BY_QUERY = "/locations/query"


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}{TEQUILA_SEARCH_BY_QUERY}"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]

        return code
