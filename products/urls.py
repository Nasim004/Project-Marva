from django.urls import path
from . import views


urlpatterns=[

    path('productlist',views.productlist,name='productlist'),




]