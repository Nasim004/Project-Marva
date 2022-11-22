import email
from msilib import change_sequence
from unicodedata import category, name
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib import messages
from home.views import home
from django.contrib.auth.models import User,auth
from django.views.decorators.cache import never_cache
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from accounts.models import user_details
from accounts.models import address


from products.models import product_details
from products.models import Category
from products.models import *





# from admins.mixins import MessageHandler
import random
from admins.CustomBackend import *
from admins.mixins import MessageHandler



PRODUCTS_PER_PAGE = 4    

# ADMIN SIDE AND LOGOUT STARTS HERE 



@never_cache
def admin_log(request):
    if request.user.is_authenticated or request.user.is_superuser:
        return redirect(admins)
    return render(request,'admin_login.html')

@never_cache
def admins(request):
    if request.user.is_superuser:
        return redirect(adminshome)
    return redirect(admin_log)
@never_cache
def adminshome(request):
    if request.user.is_superuser:
        p=product_details.objects.all()
        return render(request,'admin.html',{'p':p})
    return redirect(admins)


@never_cache
def admin_login(request):
    if request.user.is_superuser:
        return redirect(admins)
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None and user.is_superuser:
            auth.login(request,user)
            return redirect(admins)
        else:
            messages.info(request, 'Inavlid Credentials')
            return redirect(admins)
    else:
        return render(request,'admin_login.html')



@never_cache
def admin_logout(request):
    if request.user.is_superuser:
        auth.logout(request)
    return redirect(admins)






@never_cache
def userlist(request):
    if request.user.is_superuser:
        # details=user_details.objects.all()
        details=User.objects.all()

        return render(request,'user_details.html',{'details':details})

@never_cache
def categorylist(request):
    if request.user.is_superuser:
        category=Category.objects.all()
        return render(request,'category.html',{'category':category})


@never_cache
def productlist(request):
    if request.user.is_superuser:
        p_details=product_details.objects.all()
        category=Category.objects.all()
        return render(request,'product_details.html',{'p_details':p_details,'category':category})

@never_cache
def offerlist(request):
    if request.user.is_superuser:
        p_offer=product_offer.objects.all()
        c_offer=cat_offer.objects.all()
        return render(request,'offer_list.html',{'p_offer':p_offer,'c_offer':c_offer})






def productinfo(request,id):
        p_details=product_details.objects.get(id=id)
        pro=product_details.objects.all()
        
        return render(request,'product_info.html',{'p':p_details,'pro':pro})



def addproduct1(request):
    if request.user.is_superuser: 
        if request.method == 'GET':
            category=Category.objects.all()
            return render(request, 'addproduct.html',{'category':category})



def addproduct(request):
    if request.method == 'POST':
        product_name=request.POST.get('product_name')  
        des=request.POST.get('des')     
        image=request.FILES['image'] 
        price=request.POST.get('price')    
        # dis_price=request.POST.get('dis_price')
        category=request.POST.get('id')
        category=Category.objects.get(id=category)  
        stock=request.POST.get('stock')
        products= product_details.objects.create(product_name=product_name,des=des,img=image,price=price,category=category,stock=stock)
        products.save()

        return redirect(productlist)





def product_delete(request,id):
    product_del=product_details.objects.get(id=id)
    product_del.delete()
    product = product_details.objects.all()
    return redirect(productlist)



def category_delete(request,id):
    product_del=Category.objects.get(id=id)
    product_del.delete()
    product = Category.objects.all()
    return redirect(categorylist)





def add_category(request):
    if request.method == 'GET':
        return render(request,'addcategory.html ')
    if request.method == 'POST':
        category_name=request.POST.get('category_name')
        category_name1=category_name[:-1]
        if Category.objects.filter(category_name__icontains=category_name):
                    messages.info(request,"Category Exist")
                    return redirect('categorylist')
        elif Category.objects.filter(category_name__icontains=category_name1):
            messages.info(request,'Category is already exist')
            return redirect('categorylist')
        category=Category.objects.create(category_name=category_name)
        category.save()
        return redirect ('categorylist')





def product_edit(request,id):
  if request.user.is_superuser:  
    p_details= product_details.objects.get(id=id)
    category=Category.objects.all()
    return render(request,'editproduct.html',{'p_details':p_details,'category':category} )


def product_update(request,id):
    if request.method == 'POST':
        product=product_details.objects.get(id=id)
        product_name=request.POST.get('product_name')  
        des=request.POST.get('des')     
        image=request.FILES.get('image',product.img)  
        price=request.POST.get('price')    
        category=request.POST.get('id')
        stock=request.POST.get('stock')
        category=Category.objects.get(id=category)  
        product.product_name=product_name
        product.des=des
        product.img=image
        product.price=price
        product.category=category
        product.stock=stock
        product.save()
        return redirect(productlist)



def product(request,id):
    category=Category.objects.get(id=id)
    c1=Category.objects.all()
    product=product_details.objects.filter(category=category).all()
    page = request.GET.get('page',1)
    product_paginator = Paginator(product, PRODUCTS_PER_PAGE)
    try:
        product = product_paginator.page(page)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)
    except:
        product = product_paginator.page(PRODUCTS_PER_PAGE)
    return render(request,'product.html',{'product':product,'page_obj':product,'is_paginated':True,'paginator':product_paginator,'c1':c1})
    



def base(request):
    category=Category.objects.all()
    user=user_details.objects.all()
    return render(request,'base.html',{'category':category,'user':user})    



def blockuser(request,id):
    user=User.objects.get(id=id)
    user.is_active=False
    user.save()
    return redirect(userlist)


def unblockuser(request,id):
    user=User.objects.get(id=id)
    user.is_active=True
    user.save()
    return redirect(userlist)




def category_edit(request,id):
  if request.user.is_superuser:  
    category= Category.objects.get(id=id)
    return render(request,'editcategory.html',{'category':category})

def category_update(request,id):
    if request.method == 'POST':
        category_name=request.POST.get('category_name')  
        category=Category.objects.get(id=id)  
        category.category_name=category_name
        category.save()
        messages.info(request,"Categroy Updated")
    return redirect('categorylist')



def number_check(request):
   if request.method=='POST' and request.POST['phone_number']:
      
       global phone
       phone=request.POST['phone_number']
       print("phone1=",phone)
       otp='123456'
       message_handler = MessageHandler(phone,otp).sent_otp_on_phone()
       return redirect('otp_validate')
   return render(request,'otplogin.html')

@never_cache
def otp_validate(request):
   if request.user.is_authenticated:
     return redirect(home)
   if request.method=='POST' and request.POST['otp']:
       otp1= int(request.POST['otp'])
       validate = MessageHandler(phone,otp1).validate()
       print("validate=",validate)
       if validate=="approved":
           user=CustomBackend.authenticate(request,phone_number=phone)
           print("-----")
           print (user)
          
           return redirect('home')
      
   return render(request,'otpcheck.html')


# OTP GENERATE SECTION END


 
def userprofile(request):
    if request.user.is_authenticated:

        details=user_details.objects.get(user=request.user.id)
        addres=address.objects.filter(user=details)
        category=Category.objects.all()

        return render(request,'userprofile.html',{'details':details,'addres':addres,'category':category})
    return render(request,'login.html')





def address_edit(request,id):
    if request.user.is_authenticated:
        add=address.objects.get(id=id)
        return render(request,'addedit.html',{'add':add})

def add_update(request,id):
    if request.method == 'POST':
        # user = request.user.user_details
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        adds = request.POST.get('adds') 
        district = request.POST.get('district')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        landmark= request.POST.get('landmark')
        type=request.POST.get('type')
        add=address.objects.get(id=id)  
        print(add)
        add.name=name
        add.phone=phone
        add.address=adds
        add.district=district
        add.state=state
        add.postcode=postcode
        add.landmark=landmark
        add.type=type
        add.save()
        return redirect(userprofile)


def add_delete(request,id):
    add_del=address.objects.get(id=id)
    add_del.delete()
    add= address.objects.all()
    return redirect(userprofile)



def user_edit(request,id):
    if request.user.is_authenticated:
        id=request.user.user_details.id
        user=user_details.objects.get(id=id)
        user1=User.objects.get(id=request.user.id)
        if request.method == 'POST':
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            phone=request.POST.get('phone')
            email=request.POST.get('email')


            user.First_name=first_name
            user.last_name=last_name
            user.phone_number=phone
            user.email=email
            user.save()
            # messages.info(request,"Profile Updated Succesfully")


            user1.username=email
            user1.first_name=first_name
            user1.last_name=last_name
            user1.save()
            messages.info(request,"Profile Updated Succesfully")
            return redirect(userprofile)     
        return render(request,'useredit.html',{'user':user})




def change_password(request):
    if request.method == 'POST':
        user = request.user
        old=request.POST['old']
        new = request.POST['new']
        confirm = request.POST['confirm']
        if new != confirm:
            messages.info(request,"The passwords are not matching")
            return redirect(change_password)
        elif not user.check_password(old):
            messages.info(request,"Wrong Old Password")
            return redirect(change_password)
        else:
            user.set_password(new)
            user.save()
            
            return redirect(userprofile)
    return render(request,'passedit.html')            


def login_resend(request):
    otp=123456
    message_handler = MessageHandler(phone,otp).sent_otp_on_phone()
    return redirect('otp_validate')

def signup_resend(request):
    otp=123456
    message_handler = MessageHandler(phone,otp).sent_otp_on_phone()
    return redirect('signup_otp_validate')



def p_offeradd(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        offer = request.POST['offer']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        product = request.POST['product']
        offer1 = product_offer.objects.create(name=name,offer=offer,start_date=startdate,end_date=enddate,offer_type='product',product_id=product)
        offer1.save()
        offer2 =product_details.objects.get(id=product)
        offer2.p_offer=offer
        offer2.save()
        p_op=product_details.objects.get(id=product)
        p_op.p_offer_price= (p_op.price)-(p_op.price*(int(offer)/100))
        p_op.save()
       

        return redirect('offerlist')
    else:
        product=product_details.objects.all()
        return render(request, "p_offeradd.html",{'product':product})


def block_p_offer(request,id):
    offer=product_offer.objects.get(id=id)
    p_id=offer.product_id
    product=product_details.objects.get(id=p_id)
    product.p_offer=0
    product.p_offer_price=0
    offer.is_active=False
    product.save()
    offer.save()
    return redirect(offerlist)


def unblock_p_offer(request,id):
    offer1=product_offer.objects.get(id=id)
    p_id=offer1.product_id
    product=product_details.objects.get(id=p_id)
    product.p_offer=offer1.offer
    product.p_offer_price=(product.price)-(product.price*(offer1.offer/100))
    offer1.is_active=True
    product.save()
    offer1.save()
    return redirect(offerlist)


def product_offer_remove(request,id):
    offer=product_offer.objects.get(id=id)
    p_id=offer.product_id
    product=product_details.objects.get(id=p_id)
    product.p_offer=0
    product.p_offer_price=0
    product.save()
    offer.delete()
    return redirect('offerlist')


def product_offer_edit(request,id): 
  if request.user.is_superuser:  
    offer= product_offer.objects.get(id=id)
    product=product_details.objects.all()
    return render(request,'edit_p_offer.html',{'offer':offer,'product':product} )


def product_offer_update(request,id):
    if request.method == 'POST':

        product1=product_offer.objects.get(id=id)

        name=request.POST.get('name')        
        offer=request.POST.get('offer')    
        product=request.POST.get('id')
        start_date=request.POST.get('startdate')    
        end_date=request.POST.get('enddate')    



        product=product_details.objects.get(id=product)  

        product1.name=name
        product1.offer=offer
        product1.product=product
        product1.start_date=start_date
        product1.end_date=end_date

        product1.save()
        return redirect(offerlist)








def c_offeradd(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        offer = request.POST['offer']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        upto=request.POST['upto']
        category = request.POST['category']
        offer1 = cat_offer.objects.create(name=name,offer=offer,start_date=startdate,end_date=enddate,up_to=upto,offer_type='category',category_id=category)
        offer1.save()
        cat=Category.objects.get(id=category)
        print(cat)
        cat.offer=offer
        cat.save()
        offer2 =product_details.objects.filter(category_id=category)
        for i in offer2:
            i.c_offer = offer
            i.c_offer_price = i.price-(i.price*(int(offer)/100))
            i.save()
        return redirect('offerlist')
    else:
        category=Category.objects.all()
        return render(request, "c_offeradd.html",{'category':category})



def block_c_offer(request,id):
    offer=cat_offer.objects.get(id=id)
    p_id=offer.category_id
    product=product_details.objects.get(category_id=p_id)
    product.c_offer=0
    product.c_offer_price=0
    offer.is_active=False
    offer.save()
    product.save()
    return redirect(offerlist)


def unblock_c_offer(request,id):
    offer1=cat_offer.objects.get(id=id)
    p_id=offer1.category_id
    product=product_details.objects.get(category_id=p_id)
    product.c_offer=offer1.offer
    product.c_offer_price=(product.price)-(product.price*(offer1.offer/100))
    offer1.is_active=True
    product.save()
    offer1.save()
    return redirect(offerlist)



def cat_offer_remove(request,id):
    offer=cat_offer.objects.get(id=id)
    p_id=offer.category_id
    category=Category.objects.get(id=p_id)
    category.c_offer=0
    category.c_offer_price=0
    category.save()
    offer.delete()
    return redirect(offerlist)


def cat_offer_edit(request,id): 
  if request.user.is_superuser:  
    offer= cat_offer.objects.get(id=id)
    category=Category.objects.all()
    return render(request,'edit_c_offer.html',{'offer':offer,'category':category} )


def cat_offer_update(request,id):
    if request.method == 'POST':

        category1=cat_offer.objects.get(id=id)

        name=request.POST.get('name')        
        offer=request.POST.get('offer')    
        category=request.POST.get('id')
        upto=request.POST.get('upto')     
        start_date=request.POST.get('startdate')    
        end_date=request.POST.get('enddate')    



        category=Category.objects.get(id=category)  

        category1.name=name
        category1.offer=offer
        category1.category=category
        category1.up_to=upto
        category1.start_date=start_date
        category1.end_date=end_date

        category1.save()
        return redirect(offerlist)








@never_cache
def couponlist(request):
    if request.user.is_superuser:
        coupon = Coupons.objects.all()
        return render(request,'coupon_list.html',{'coupon':coupon,})





def coupon_add(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        minamount=request.POST['minamount']
        disamount=request.POST['disamount']


        c = Coupons.objects.create(name=name,code=code,start_date=startdate,end_date=enddate,min_amount=minamount,discount_amount=disamount)
        c.save()
        return redirect(couponlist)

    else:
        c=Coupons.objects.all()
        return render(request, "coupon_add.html",{'c':c})


def block_coupon(request,id):
    c=Coupons.objects.get(id=id)
    c.is_active=False
    c.save()
    return redirect(couponlist)


def unblock_coupon(request,id):
    c=Coupons.objects.get(id=id)
    c.is_active=True
    c.save()
    return redirect(couponlist)



def coupon_delete(request,id):
    c=Coupons.objects.get(id=id)
    c.delete()
    return redirect(couponlist)


def coupon_edit(request,id): 
  if request.user.is_superuser:  
    coupon= Coupons.objects.get(id=id)
    return render(request,'coupon_edit.html',{'coupon':coupon} )


def coupon_update(request,id):
    if request.method == 'POST':

        coupon=Coupons.objects.get(id=id)

        name=request.POST.get('name')        
        minamount=request.POST.get('minamount')    
        disamount=request.POST.get('disamount')     
        start_date=request.POST.get('startdate')    
        end_date=request.POST.get('enddate')    
        code=request.POST.get('code')



       

        coupon.name=name
        coupon.min_amount=minamount
        coupon.discount_amount=disamount
        coupon.start_date=start_date
        coupon.end_date=end_date
        coupon.code=code
        coupon.save()
        return redirect(couponlist)

