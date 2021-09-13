from twilio.rest import Client
import smtplib
import os

class NotificationManager:

    def text_notification(self, price, city1, code1, city2, code2, date1, date2):
        
        account_sid = os.environ['Enter your Twilio Account_SID']
        auth_token = os.environ['Enter your Twilio Auth_Token']
        phone_number = os.environ['Enter your phone number']
        twilio_number = os.environ['Enter your Twilio account phone number']


        client = Client(account_sid, auth_token)
        message = client.messages \
                    .create(
                        body=f"Low price alert! Only ${price} to fly from {city1}-{code1} to {city2}-{code2}, from {date1} to {date2}",
                        from_=twilio_number,
                        to=phone_number
        )
        print(message.status)

    def email_notification(self, emails,message, link):
      from_email = os.environ['Enter your email address']
      from_email_password = os.environ['Enter your email password']

      with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_email_password)
        for email in emails:
          connection.sendmail(from_addr=from_email, to_addrs=email, msg=f"Subject:New Low Price Flight!\n\n{message}\n{link}")