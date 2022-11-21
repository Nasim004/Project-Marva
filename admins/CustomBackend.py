from django.contrib.auth.backends import BaseBackend
from accounts.models import user_details
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth,User

# User = get_user_model()

class CustomBackend(BaseBackend):
   def authenticate(request, phone_number):
       # Check the token and return a user.
       try:
        #    phone_number=phone_number[3:]  
           print(phone_number)
           user1 = user_details.objects.get(phone_number=phone_number)
           user=User.objects.get(id=user1.user_id)
           auth.login(request,user,backend='django.contrib.auth.backends.ModelBackend')

       except user.DoesNotExist:
           return None
