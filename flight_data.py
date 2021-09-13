class FlightData:
    def flight_data(flight):
        try:
            data = flight['data'][0]
            price = data['price']
            link = data['deep_link']

            departure_date = data['route'][0]['local_departure']
            return_date = data['route'][-1]['local_arrival']

            return {'price': price, 'departure': departure_date[0:10], 'return': return_date[0:10], 'link': link}
        except:
            pass


