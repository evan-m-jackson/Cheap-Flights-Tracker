from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os

f_data = FlightData()
f_search = FlightSearch()
d_manager = DataManager()
notification = NotificationManager()
sheet_data = d_manager.getting_rows()
email_data = d_manager.get_customer_emails()

current_date = datetime.today()
future_date = current_date + relativedelta(months=6)


HOME_CITY = os.environ['Add your origin city']
HOME_CODE = f_search.get_code(HOME_CITY)
FROM_DATE = current_date.strftime("%d/%m/%Y")
TO_DATE = future_date.strftime("%d/%m/%Y")

for row in sheet_data:
  
    if row['iataCode'] == "":
        code = f_search.get_code(row['city'])
        d_manager.edit_a_row(row['id'], iataCode=code)

    flight = f_search.get_flight(row['iataCode'], HOME_CODE, FROM_DATE, TO_DATE)
    
    if flight is None:
      continue
    
    if flight['price'] < row["lowestPrice"]:
      emails = [e['email'] for e in email_data]
      message = f"Low price alert! Only ${flight['price']} to fly from {HOME_CITY}-{HOME_CODE} to {row['city']}-{row['iataCode']}, from {flight['departure']} to {flight['return']}"
      google_link = flight['link']
      send_email = notification.email_notification(emails, message, google_link)
      
    
    
