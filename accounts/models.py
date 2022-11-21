from email.policy import default
from enum import unique
from sre_parse import State
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class user_details(models.Model):
    First_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15,unique=True)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=100)
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)



class address(models.Model):

    type=models.CharField(max_length=20)
    user=models.ForeignKey(user_details,on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    postcode=models.IntegerField()
    district=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    landmark=models.CharField(max_length=20,null=True)


    

