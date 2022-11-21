from email.headerregistry import Address
from email.policy import default
from django.db import models
from accounts.models import address, user_details,User
from admins.views import product
from products.models import product_details
# Create your models here.


class Cart(models.Model):
    quantity=models.IntegerField(default=1)
    user=models.ForeignKey(user_details,on_delete=models.CASCADE)
    product=models.ForeignKey(product_details,on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)



class guestCart(models.Model):
    quantity=models.IntegerField(default=1)
    user_ref=models.CharField(max_length=200,null=True,blank=True)
    product=models.ForeignKey(product_details,on_delete=models.CASCADE)
    


class Order(models.Model):
    user=models.ForeignKey(user_details,on_delete=models.CASCADE)
    address=models.ForeignKey(address,on_delete=models.CASCADE)
    order_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default='confirmed')
    amount = models.FloatField(default=1)
    method= models.CharField(max_length=100,default='cash on delivery')


class oldcart(models.Model):    
    quantity = models.IntegerField(default=1)
    user=models.ForeignKey(user_details,on_delete=models.CASCADE)
    product=models.ForeignKey(product_details,on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,default=0)
    total = models.IntegerField(default=1)



    def __str__(self):
        return self.product.product_name