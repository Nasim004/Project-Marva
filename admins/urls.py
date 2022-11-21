from unicodedata import name
from django.urls import path
from . import views



urlpatterns=[

    path('',views.admins,name='admins'),
    path('admin_log',views.admin_log,name='admin_log'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    
    path('userlist',views.userlist,name='userlist'),
    path('productlist',views.productlist,name='productlist'),

    
    path('categorylist',views.categorylist,name='categorylist'),
    path('offerlist',views.offerlist,name='offerlist'),
    path('couponlist',views.couponlist,name='couponlist'),




    path('adminshome',views.adminshome,name='adminshome'),

    path('addproduct1',views.addproduct1,name='addproduct1'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('p_offeradd',views.p_offeradd,name='p_offeradd'),
    path('c_offeradd',views.c_offeradd,name='c_offeradd'),
    path('coupon_add',views.coupon_add,name='coupon_add'),




    path('category',views.category,name='category'),
    path('add_category',views.add_category,name='add_category'),

    path('product_delete/<int:id>',views.product_delete,name='product_delete'),
    path('category_delete/<int:id>',views.category_delete,name='category_delete'),
    path('product_offer_remove/<int:id>',views.product_offer_remove,name='product_offer_remove'),
    path('cat_offer_remove/<int:id>',views.cat_offer_remove,name='cat_offer_remove'),







    path('product_edit/<int:id>',views.product_edit,name='product_edit'),
    path('product_update/<int:id>',views.product_update,name='product_update'),
    path('product/<int:id>',views.product,name='product'),

    path('blockuser/<int:id>',views.blockuser,name='blockuser'),
    path('unblockuser/<int:id>',views.unblockuser,name='unblockuser'),


    path('block_p_offer/<int:id>',views.block_p_offer,name='block_p_offer'),
    path('unblock_p_offer/<int:id>',views.unblock_p_offer,name='unblock_p_offer'),

    path('block_c_offer/<int:id>',views.block_c_offer,name='block_c_offer'),
    path('unblock_c_offer/<int:id>',views.unblock_c_offer,name='unblock_c_offer'),

    path('block_coupon/<int:id>',views.block_coupon,name='block_coupon'),
    path('unblock_coupon/<int:id>',views.unblock_coupon,name='unblock_coupon'),







    path('productinfo/<int:id>',views.productinfo,name='productinfo'),

    path('category_edit/<int:id>',views.category_edit,name='category_edit'),
    path('category_update/<int:id>',views.category_update,name='category_update'),

    path('number_check',views.number_check,name='number_check'),
    path('otp_validate',views.otp_validate,name='otp_validate'),



    path('userprofile',views.userprofile,name='userprofile'),
 
    path('address_edit/<int:id>',views.address_edit,name='address_edit'),
    path('add_update/<int:id>',views.add_update,name='add_update'),
    path('add_delete/<int:id>',views.add_delete,name='add_delete'),
    path('user_edit/<int:id>',views.user_edit,name='user_edit'),
    path('change_password',views.change_password,name='change_password'),


    path('login_resend', views.login_resend, name="login_resend"),

    







    






    

]