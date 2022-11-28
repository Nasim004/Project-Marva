from unicodedata import name
from django.urls import path
from . import views



urlpatterns=[

    path('cart',views.cart,name='cart'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('addtocart2/<int:id>',views.addtocart2,name='addtocart2'),
    path('minus/<int:id>',views.minus,name='minus'),
    path('up/<int:id>',views.up,name='up'),
    path('removecart/<int:id>',views.removecart,name='removecart'),
    path('checkout',views.checkout,name='checkout'),
    path('addaddress',views.addaddress,name='addaddress'),
    path('addaddress1',views.addaddress,name='addaddress'),
    path('orderlist',views.orderlist,name='orderlist'),
    path('saleslist',views.saleslist,name='saleslist'),
    path('myorder',views.myorder,name='myorder'),

    path('ordercancel/<int:id>',views.ordercancel,name='ordercancel'),
    path('orderreturn/<int:id>',views.orderreturn,name='orderreturn'),
    path('orderupdate/<int:id>',views.orderupdate,name='orderupdate'),
    path('orderplaced',views.orderplaced,name='orderplaced'),


    path('date_select',views.date_select, name='date_select'),
    path('monthly_sales',views.monthly_sales, name='monthly_sales'),
    path('yearly_sales',views.yearly_sales, name='yearly_sales'),

    path('report',views.report, name='report'),
    
    path('razorpay',views.razorpay,name='razorpay'),


    path('invoice/<int:id>',views.invoice,name='invoice'),




    

        

]