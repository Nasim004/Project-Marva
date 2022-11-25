
from wsgiref import validate
from django.shortcuts import render,redirect
from django.contrib import messages
from admins.mixins import MessageHandler
# from Marva.admins.views import otp_validate
from home.views import home
from .models import user_details
from django.contrib.auth.models import User,auth
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
# from admins.views import signup_otp_validate

from cart.models import guestCart,Cart





@never_cache
def login(request): 
        if request.method=='POST':
            email=request.POST.get('email')
            print(email)
            password=request.POST.get('password')
            print
            user=auth.authenticate(username=email,password=password)
            print(user)
            if user is not None and user.is_active :
                if 'guest_key' in request.session:
                    p = request.session['guest_key']
                    guest_cart = guestCart.objects.filter(user_ref=p)

                    auth.login(request, user)
                    for i in guest_cart:
                        try:
                            cart = Cart.objects.get(user=request.user.user_details,product=i.product)
                            print(cart)
                        except:
                            cart = None
                        if cart:
                            print("one")
                            Cart.objects.filter(user=request.user.user_details, product=i.product).update(quantity = cart.quantity+i.quantity)
                        else:
                            print("two")
                            k = Cart(user=request.user.user_details,product=i.product,quantity=i.quantity)
                            k.save()
                    print("deleting guest cart")
                    guest_cart.delete()
                auth.login(request,user)
                return redirect('home')
            messages.error(request,'Invalid Credetials')
            return redirect('login')


                       
          
        return render(request,'login.html')     
        



@never_cache
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(home)








@never_cache
def register(request):
    
    if request.user.is_authenticated:
       return redirect(home)
    if request.method=='POST':


       
       first_name=request.POST['first_name']
       last_name=request.POST['last_name']
       email=request.POST['email']
       phone_number=request.POST['phone_number']
       password=request.POST.get('password')
       password2=request.POST.get('password1')
       print('phone===',phone_number)
       


       if password==password2:
            print('hiii')
            if not first_name.isalpha():
                messages.error(request,'Only letters are to be entered in name')
                
                print('1')
                return redirect(register)
                
            elif len(phone_number)<10 or len(phone_number)>14:
                messages.error(request,'Mobile Or Phone number is wrong')
                print('2')

                return redirect(register)
            elif user_details.objects.filter(email=email).exists() or user_details.objects.filter(phone_number=phone_number).exists():
                messages.error(request,'Already taken user')
                return redirect(register)
            
            else:
                print('hii')
                otp=1
                message_handler=MessageHandler(phone_number,otp).sent_otp_on_phone()
                context = {'first_name':first_name,'last_name':last_name,'email':email,'phone_number':phone_number,'password':password}
                return render(request,'otpsignincheck.html',context)
       else:
                    messages.info(request,'!! The password is not matching !!')
                    return redirect('register')
    else:
        return render(request,'register.html')

                




def otp_validate_reg(request):
    if request.method=='POST' and request.POST['otp']:
        otp1=request.POST.get('otp')
        print(otp1)
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        password=request.POST.get('password')
        validate=MessageHandler(phone_number,otp1).validate()
        if validate=='approved':
            user=User.objects.create_user(email=email,password=password,first_name=first_name,last_name=last_name,username=email)
            user.save()
            user1=user_details.objects.create(password=password,email=email,First_name=first_name,last_name=last_name,phone_number=phone_number,user=user)
            user1.save()
            if 'guest_key' in request.session:
                    p = request.session['guest_key']
                    guest_cart = guestCart.objects.filter(user_ref=p)

                    auth.login(request, user)
                    for i in guest_cart:
                        try:
                            cart = Cart.objects.get(user=request.user.user_details,product=i.product)
                            print(cart)
                        except:
                            cart = None
                        if cart:
                            print("one")
                            Cart.objects.filter(user=request.user.user_details, product=i.product).update(quantity = cart.quantity+i.quantity)
                        else:
                            print("two")
                            k = Cart(user=request.user.user_details,product=i.product,quantity=i.quantity)
                            k.save()
                    print("deleting guest cart")
                    guest_cart.delete()
                    

            messages.info(request,"Acoount Created")
            return redirect('home')

    return render(request,'otpsignincheck.html')



# USER SIDE LOGIN / REGISTER AND LOGOUT ENDS HERE 
def signup_resend(request,phone_number):
    otp=123456
    message_handler = MessageHandler(phone_number,otp).sent_otp_on_phone()
    return redirect('otp_validate_reg')