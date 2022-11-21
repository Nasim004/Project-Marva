from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Category(models.Model):
    category_name=models.CharField(max_length=20)
    offer=models.FloatField(default=0)

   


    def __str__(self):
        return self.category_name   

class product_details(models.Model):
    product_name=models.CharField(max_length=50)
    des=models.CharField(max_length=200)
    img=models.ImageField(upload_to='assets/images')  
    price=models.IntegerField()
    stock=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    p_offer=models.FloatField(default=0)
    p_offer_price=models.FloatField(default=0)  
    c_offer=models.FloatField(default=0)
    c_offer_price=models.FloatField(default=0)


    def __str__(self):
        return self.product_name   
   

class product_offer(models.Model):
    product=models.ForeignKey(product_details,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    offer = models.FloatField()
    offer_type = models.CharField(max_length=200,default='Product')
    start_date = models.DateField()
    end_date = models.DateField()
    is_active=models.BooleanField(default=True)




class cat_offer(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    offer = models.FloatField()
    offer_type = models.CharField(max_length=200,default='Category')
    start_date = models.DateField()
    end_date = models.DateField()
    up_to = models.FloatField()
    is_active=models.BooleanField(default=True)



class Coupons(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    min_amount = models.FloatField()
    discount_amount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active=models.BooleanField(default=True)
  










