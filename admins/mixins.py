from django.conf import settings
from twilio.rest import Client
import random

class MessageHandler:
   phone_number = None
   otp = None
   def __init__(self,phone_number,otp)->None:
       self.phone_number = phone_number
       self.otp = otp
       print("generated otp=",self.otp)

   def sent_otp_on_phone(self):
       client=Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
       verification = client.verify \
                    .v2 \
                    .services('VA00cc0f49d98e9be3226d32d97b0ef70d') \
                    .verifications \
                    .create(to=self.phone_number, channel='sms')

   def validate(self):
       client=Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)
       verification_check = client.verify \
                          .v2 \
                          .services('VA00cc0f49d98e9be3226d32d97b0ef70d') \
                          .verification_checks \
                          .create(to=self.phone_number,code=self.otp)
       validation=verification_check.status
       print(  validation)
       return validation
