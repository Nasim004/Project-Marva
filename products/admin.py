from django.contrib import admin
from products.models import product_offer,cat_offer,Coupons
# Register your models here.
admin.site.register(product_offer)
admin.site.register(cat_offer)
admin.site.register(Coupons)


