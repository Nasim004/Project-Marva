from django.contrib import admin
from cart.models import Order,oldcart
# Register your models here.
admin.site.register(Order)
admin.site.register(oldcart)

