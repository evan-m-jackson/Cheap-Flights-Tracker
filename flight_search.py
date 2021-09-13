import requests
import os
from flight_data import FlightData

class FlightSearch:
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com"
        self.apikey = os.environ['Enter your uniqie Twilio API Key']



    def get_code(self,city):
        headers = {"apikey": self.apikey}

        params = {
            "term": city
        }
        response = requests.get(url=f"{self.endpoint}/locations/query", params=params, headers=headers)
        response.raise_for_status()
        try:
          data = response.json()
        except KeyError:
          return None
        else:
          return data['locations'][0]['code']

    def get_flight(self, destination_code, origin_code, from_date, to_date):

        headers = {"apikey": self.apikey}

        params = {
           "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": from_date,
            "date_to": to_date,
            "curr": 'USD',
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 21,
            "flight_type": 'round',
            "one_for_city": 1
        }
        response = requests.get(url=f"{self.endpoint}/v2/search", params=params, headers=headers)
        response.raise_for_status()

        try:
          data = response.json()
        except IndexError:
          return None
        else:
          flight = FlightData.flight_data(data)
          return flight



