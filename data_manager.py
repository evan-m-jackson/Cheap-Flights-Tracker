import requests
import os

class DataManager:

    def __init__(self):
        self.endpoint = os.environ['Prices Sheet URL']


    def getting_rows(self):
        response = requests.get(url=self.endpoint)
        response.raise_for_status()
        data = response.json()
        return data["prices"]

    def adding_rows(self, CITY, CODE, PRICE):
        params = {
            "price": {
                "city": CITY,
                "iataCode": CODE,
                "lowestPrice": PRICE
            }
        }
        response = requests.post(url=self.endpoint, json=params)
        print(response.text)

    def edit_a_row(self, row, **kwargs):
        params = {"price": {}}
        for key, value in kwargs.items():
            params["price"][key] = value
        response = requests.put(url=f"{self.endpoint}/{row}", json=params)
        print(response.text)
    
    def get_customer_emails(self):
      users_endpoint = os.environ['User Sheet URL']
      response = requests.get(users_endpoint)
      data = response.json()
      return data['users']

