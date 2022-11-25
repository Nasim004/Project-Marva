from django.urls import path
from . import views


urlpatterns=[

    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('otp_validate_reg',views.otp_validate_reg,name='otp_validate_reg'),
    path('signup_resend/<str:phone_number>', views.signup_resend, name="signup_resend"),
    


    
    

]