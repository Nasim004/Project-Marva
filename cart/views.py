from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.views.decorators.cache import never_cache

from admins.views import userprofile
from products.models import Coupons
from .models import *
from django.http import JsonResponse, HttpResponse

from accounts.models import address
from cart.models import oldcart


from products.models import Category



@never_cache
def cart(request):
    c1=Category.objects.all()
    if request.user.is_authenticated and request.user.is_active :
        user = request.user.user_details
        

        if Cart.objects.filter(user=user):

            cart = Cart.objects.filter(user=user)

            for i in range(len(cart)):

                if cart[i].quantity <= 0:
                    cart[i].delete()
            if len(cart) == 0:
                empty = "Cart is Empty"
                return render(request, 'cart.html', {'empty': empty})
            else:
                subtotal = 0
                for i in range(len(cart)):
                 if cart[i].cancel != True:

                    if cart[i].product.p_offer_price < 1 and  cart[i].product.c_offer_price < 1:
                        x = cart[i].product.price*cart[i].quantity
                        subtotal = subtotal+x
                    elif cart[i].product.p_offer_price > 1 and  cart[i].product.c_offer_price == 0:
                        x = cart[i].product.p_offer_price*cart[i].quantity
                        subtotal = subtotal+x
                    elif cart[i].product.p_offer_price < 1 and  cart[i].product.c_offer_price > 1:
                        x = cart[i].product.c_offer_price*cart[i].quantity
                        subtotal = subtotal+x
                    elif cart[i].product.p_offer_price < cart[i].product.c_offer_price and cart[i].product.c_offer_price > 1:
                        x = cart[i].product.p_offer_price*cart[i].quantity
                        subtotal = subtotal+x
                    elif cart[i].product.c_offer_price < cart[i].product.p_offer_price and cart[i].product.p_offer_price > 1:
                        x = cart[i].product.c_offer_price*cart[i].quantity
                        subtotal = subtotal+x
                    elif cart[i].product.p_offer_price == cart[i].product.c_offer_price and cart[i].product.c_offer_price > 1 and cart[i].product.p_offer_price > 1:
                        x = cart[i].product.p_offer_price*cart[i].quantity
                        subtotal = subtotal+x

                shipping = 0
                total = subtotal + shipping
                return render(request, 'cart.html', {'cart': cart, 'subtotal': subtotal, 'total': total,'c1':c1})
        return render(request, 'cart.html', {'message':"CART IS EMPTY",'c1':c1})      
    else:
        c1=Category.objects.all()
        if not request.session.session_key:
            request.session.create()
        request.session['guest_key']=request.session.session_key
        key = request.session['guest_key']
        cart = guestCart.objects.filter(user_ref=request.session.session_key)
        subtotal = 0
        for i in range(len(cart)):
                 

                    if cart[i].product.p_offer_price < 1 and  cart[i].product.c_offer_price < 1:
                        x = cart[i].product.price*cart[i].quantity
                        subtotal = subtotal+x
                    elif cart[i].product.p_offer_price > 1 and  cart[i].product.c_offer_price == 0:
                        x = cart[i].product.p_offer_price*cart[i].quantity
                        subtotal = subtotal+x
                    elif cart[i].product.p_offer_price < 1 and  cart[i].product.c_offer_price > 1:
                        x = cart[i].product.c_offer_price*cart[i].quantity
                        subtotal = subtotal+x
                    elif cart[i].product.p_offer_price < cart[i].product.c_offer_price and cart[i].product.c_offer_price > 1:
                        x = cart[i].product.p_offer_price*cart[i].quantity
                        subtotal = subtotal+x
                    elif cart[i].product.c_offer_price < cart[i].product.p_offer_price and cart[i].product.p_offer_price > 1:
                        x = cart[i].product.c_offer_price*cart[i].quantity
                        subtotal = subtotal+x
                    elif cart[i].product.p_offer_price == cart[i].product.c_offer_price and cart[i].product.c_offer_price > 1 and cart[i].product.p_offer_price > 1:
                        x = cart[i].product.p_offer_price*cart[i].quantity
                        subtotal = subtotal+x

        shipping = 0
        total = subtotal + shipping
        return render(request, 'cart.html', {'cart': cart, 'subtotal': subtotal, 'total': total,'c1':c1})    




def addtocart(request,id):
    if request.user.is_authenticated:
        product = product_details.objects.get(id=id)
        uid = request.user.user_details
        if Cart.objects.filter(product=id, user=uid).exists():
            cart = Cart.objects.get(product=id, user=uid)
            cart.quantity = cart.quantity+1
            cart.save()
            return redirect('cart')
        else:
            cart = Cart.objects.create(product=product, user=uid)
            return redirect('cart')
    else:
        if not request.session.session_key:
            request.session.create()
        product = product_details.objects.get(id=id)
        # uid = request.user
        if guestCart.objects.filter(product=id,user_ref=request.session.session_key).exists():
            cart = guestCart.objects.get(product=id,)
            cart.quantity = cart.quantity+1
            cart.save()
            return redirect('cart')
        else:
            cart = guestCart.objects.create(product=product, user_ref=request.session.session_key)
            return redirect('cart')



def up(request,id):
    if request.user.is_authenticated:
  
        crt = Cart.objects.filter(user=request.user.user_details)
        cart = Cart.objects.get(id=id)
        qty = int(cart.quantity)+1
        Cart.objects.filter(id=id).update(quantity=qty)
        subtotal = 0
        for i in crt:

            
            if i.product.p_offer_price < 1 and  i.product.c_offer_price < 1:
                            x = i.product.price*i.quantity
                            subtotal = subtotal+x
            elif i.product.p_offer_price > 1 and  i.product.c_offer_price == 0:
                            x = i.product.p_offer_price*i.quantity
                            subtotal = subtotal+x
            elif i.product.p_offer_price < 1 and  i.product.c_offer_price > 1:
                            x = i.product.c_offer_price*i.quantity
                            subtotal = subtotal+x
            elif i.product.p_offer_price < i.product.c_offer_price and i.product.c_offer_price > 1:
                            x = i.product.p_offer_price*i.quantity
                            subtotal = subtotal+x
            elif i.product.c_offer_price < i.product.p_offer_price and i.product.p_offer_price > 1:
                            x = i.product.c_offer_price*i.quantity
                            subtotal = subtotal+x
            elif i.product.p_offer_price == i.product.c_offer_price and i.product.c_offer_price > 1 and i.product.p_offer_price > 1:
                            x = i.product.p_offer_price*i.quantity
                            subtotal = subtotal+x

        shipping = 0
        total = subtotal + shipping
        return JsonResponse({'qty': qty,'total':total,'subtotal':subtotal})

    else:    
        crt = guestCart.objects.filter(user_ref=request.session.session_key)
        cart = guestCart.objects.get(id=id)
        qty = int(cart.quantity)+1
        guestCart.objects.filter(id=id).update(quantity=qty)
         
        subtotal = 0
        for i in crt:

            
            if i.product.p_offer_price < 1 and  i.product.c_offer_price < 1:
                            x = i.product.price*i.quantity
                            subtotal = subtotal+x
            elif i.product.p_offer_price > 1 and  i.product.c_offer_price == 0:
                            x = i.product.p_offer_price*i.quantity
                            subtotal = subtotal+x
            elif i.product.p_offer_price < 1 and  i.product.c_offer_price > 1:
                            x = i.product.c_offer_price*i.quantity
                            subtotal = subtotal+x
            elif i.product.p_offer_price < i.product.c_offer_price and i.product.c_offer_price > 1:
                            x = i.product.p_offer_price*i.quantity
                            subtotal = subtotal+x
            elif i.product.c_offer_price < i.product.p_offer_price and i.product.p_offer_price > 1:
                            x = i.product.c_offer_price*i.quantity
                            subtotal = subtotal+x
            elif i.product.p_offer_price == i.product.c_offer_price and i.product.c_offer_price > 1 and i.product.p_offer_price > 1:
                            x = i.product.p_offer_price*i.quantity
                            subtotal = subtotal+x

        shipping = 0
        total = subtotal + shipping
        return JsonResponse({'qty': qty,'total':total,'subtotal':subtotal})

def minus(request,id):

        if request.user.is_authenticated:

            cart = Cart.objects.get(id=id)
            qty = int(cart.quantity)-1
            crt = Cart.objects.filter(user=request.user.user_details)
            Cart.objects.filter(id=id).update(quantity=qty)
            subtotal = 0
            for i in crt:
                if i.product.p_offer_price < 1 and  i.product.c_offer_price < 1:
                                x = i.product.price*i.quantity
                                subtotal = subtotal+x
                elif i.product.p_offer_price > 1 and  i.product.c_offer_price == 0:
                                x = i.product.p_offer_price*i.quantity
                                subtotal = subtotal+x
                elif i.product.p_offer_price < 1 and  i.product.c_offer_price > 1:
                                x = i.product.c_offer_price*i.quantity
                                subtotal = subtotal+x
                elif i.product.p_offer_price < i.product.c_offer_price and i.product.c_offer_price > 1:
                                x = i.product.p_offer_price*i.quantity
                                subtotal = subtotal+x
                elif i.product.c_offer_price < i.product.p_offer_price and i.product.p_offer_price > 1:
                                x = i.product.c_offer_price*i.quantity
                                subtotal = subtotal+x
                elif i.product.p_offer_price == i.product.c_offer_price and i.product.c_offer_price > 1 and i.product.p_offer_price > 1:
                                x = i.product.p_offer_price*i.quantity
                                subtotal = subtotal+x
        
            total = subtotal
            return JsonResponse({'qty': qty,'total':total,'subtotal':subtotal})
        else:
            crt = guestCart.objects.filter(user_ref=request.session.session_key)
            cart = guestCart.objects.get(id=id)
            qty = int(cart.quantity)-1
            guestCart.objects.filter(id=id).update(quantity=qty)
            subtotal = 0
            for i in crt:
                if i.product.p_offer_price < 1 and  i.product.c_offer_price < 1:
                                x = i.product.price*i.quantity
                                subtotal = subtotal+x
                elif i.product.p_offer_price > 1 and  i.product.c_offer_price == 0:
                                x = i.product.p_offer_price*i.quantity
                                subtotal = subtotal+x
                elif i.product.p_offer_price < 1 and  i.product.c_offer_price > 1:
                                x = i.product.c_offer_price*i.quantity
                                subtotal = subtotal+x
                elif i.product.p_offer_price < i.product.c_offer_price and i.product.c_offer_price > 1:
                                x = i.product.p_offer_price*i.quantity
                                subtotal = subtotal+x
                elif i.product.c_offer_price < i.product.p_offer_price and i.product.p_offer_price > 1:
                                x = i.product.c_offer_price*i.quantity
                                subtotal = subtotal+x
                elif i.product.p_offer_price == i.product.c_offer_price and i.product.c_offer_price > 1 and i.product.p_offer_price > 1:
                                x = i.product.p_offer_price*i.quantity
                                subtotal = subtotal+x
        
            total = subtotal
            return JsonResponse({'qty': qty,'total':total,'subtotal':subtotal})


def removecart(request,id):
    print(id)
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('cart')

def checkout(request):
 c1=Category.objects.all()
 if request.user.is_authenticated:
 
    if request.method == 'POST' and 'address_id' in request.POST   :
        address_id = request.POST['address_id']
        payment = request.POST['payment_selector']
        user= request.user.user_details
        print('***********************************')
        print(user)
        add = address.objects.get(id=address_id)
        cart = Cart.objects.filter(user=request.user.user_details)
        subtotal = 0
        for i in cart:
            if i.product.p_offer_price < 1 and  i.product.c_offer_price < 1:
                        x = i.product.price*i.quantity
                        subtotal = subtotal+x
            elif i.product.p_offer_price > 1 and  i.product.c_offer_price == 0:
                        x = i.product.p_offer_price*i.quantity
                        subtotal = subtotal+x
            elif i.product.p_offer_price < 1 and  i.product.c_offer_price > 1:
                        x = i.product.c_offer_price*i.quantity
                        subtotal = subtotal+x
            elif i.product.p_offer_price < i.product.c_offer_price and i.product.c_offer_price > 1:
                        x = i.product.p_offer_price*i.quantity
                        subtotal = subtotal+x
            elif i.product.c_offer_price < i.product.p_offer_price and i.product.p_offer_price > 1:
                        x = i.product.c_offer_price*i.quantity
                        subtotal = subtotal+x
            elif i.product.p_offer_price == i.product.c_offer_price and i.product.c_offer_price > 1 and i.product.p_offer_price > 1:
                        x = i.product.p_offer_price*i.quantity
                        subtotal = subtotal+x
            
        total = subtotal
        print(total)
        for i in cart:

         order = Order.objects.create(user=user, address=add, amount=total, method=payment)
         print(order,'**********************************')
         order.save()
         oldcart1 = oldcart.objects.create(
         user=user, quantity=i.quantity, product=i.product, order=order , total=i.quantity*i.product.price)
         oldcart1.save()
         product=product_details.objects.get(id=i.product_id)
         product.stock=product.stock-i.quantity
         product.save()
        cart.delete()
        print("cart done")
        return render(request,'placed.html')

    elif request.method == 'POST' and 'code' in request.POST  :
        c1=Category.objects.all()
        user = request.user.user_details
        code = request.POST['code']
        cart = Cart.objects.filter(user=user)
        if len(cart)!=0:
            add = address.objects.filter(user=user)
            subtotal = 0
            for i in cart:
                if i.product.p_offer_price < 1 and  i.product.c_offer_price < 1:
                        x = i.product.price*i.quantity
                        subtotal = subtotal+x
                elif i.product.p_offer_price > 1 and  i.product.c_offer_price == 0:
                        x = i.product.p_offer_price*i.quantity
                        subtotal = subtotal+x
                elif i.product.p_offer_price < 1 and  i.product.c_offer_price > 1:
                        x = i.product.c_offer_price*i.quantity
                        subtotal = subtotal+x
                elif i.product.p_offer_price < i.product.c_offer_price and i.product.c_offer_price > 1:
                        x = i.product.p_offer_price*i.quantity
                        subtotal = subtotal+x
                elif i.product.c_offer_price < i.product.p_offer_price and i.product.p_offer_price > 1:
                        x = i.product.c_offer_price*i.quantity
                        subtotal = subtotal+x
                elif i.product.p_offer_price == i.product.c_offer_price and i.product.c_offer_price > 1 and i.product.p_offer_price > 1:
                        x = i.product.p_offer_price*i.quantity
                        subtotal = subtotal+x
            total = subtotal
            try:
                coupon = Coupons.objects.get(code=code)

            except:
                messages.info(request,'Invalid Code')
                return render(request,'checkout.html',{'subtotal': subtotal, 'total': total, 'address': add})
            if coupon.is_active:
                if total > coupon.min_amount:
                    total =total - coupon.discount_amount
                    messages.info(request,"Coupon Discount Of %s Applied" % coupon.discount_amount)
                    print(total)
                else:
                    messages.info(request,'The minimum amount not reached')
                    return render(request,'checkout.html',{'subtotal': subtotal, 'total': total, 'address': add,'coupon':coupon,'c1':c1}) 
            else:
                messages.info(request,'Coupon Expired') 
        return render(request,'checkout.html',{'subtotal': subtotal, 'total': total, 'address': add,'coupon':coupon,'c1':c1})       
    
    else:
        c1=Category.objects.all()
        user = request.user.user_details
        cart = Cart.objects.filter(user=user)
        if len(cart)!=0:
            add = address.objects.filter(user=user)
            subtotal = 0
            for i in cart:
                if i.product.p_offer_price < 1 and  i.product.c_offer_price < 1:
                        x = i.product.price*i.quantity
                        subtotal = subtotal+x
                elif i.product.p_offer_price > 1 and  i.product.c_offer_price == 0:
                        x = i.product.p_offer_price*i.quantity
                        subtotal = subtotal+x
                elif i.product.p_offer_price < 1 and  i.product.c_offer_price > 1:
                        x = i.product.c_offer_price*i.quantity
                        subtotal = subtotal+x
                elif i.product.p_offer_price < i.product.c_offer_price and i.product.c_offer_price > 1:
                        x = i.product.p_offer_price*i.quantity
                        subtotal = subtotal+x
                elif i.product.c_offer_price < i.product.p_offer_price and i.product.p_offer_price > 1:
                        x = i.product.c_offer_price*i.quantity
                        subtotal = subtotal+x
                elif i.product.p_offer_price == i.product.c_offer_price and i.product.c_offer_price > 1 and i.product.p_offer_price > 1:
                        x = i.product.p_offer_price*i.quantity
                        subtotal = subtotal+x
            total = subtotal
            return render(request, 'checkout.html', {'subtotal': subtotal, 'total': total, 'address': add,'c1':c1})
        messages.error(request, 'Cart is empty')
        return redirect('cart')
 return redirect ('login')







def addaddress(request):
  if request.user.is_authenticated:  

    if request.method == 'POST':
        print("form post method")
        user = request.user.user_details
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        add = request.POST.get('add')
        district = request.POST.get('district')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        landmark= request.POST.get('landmark')
        type=request.POST.get('type')
        new_address = address.objects.create(name=name,type=type, phone=phone, address=add, district=district, state=state, postcode=postcode, user=user,landmark=landmark)
        new_address.save()
        print("saved address")
        return redirect('checkout')
    else:
        return render(request,'addaddress.html')
  return render(request,'landingpage.html')




def addaddress1(request):
  if request.user.is_authenticated:  
    if request.method == 'POST':
        print("form post method")
        user = request.user.user_details
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        add = request.POST.get('add')
        district = request.POST.get('district')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        landmark= request.POST.get('landmark')
        type=request.POST.get('type')
        new_address = address.objects.create(name=name,type=type, phone=phone, address=add, district=district, state=state, postcode=postcode, user=user,landmark=landmark)
        new_address.save()
        print("saved address")
        return redirect('userprofile')
    else:
        return render(request,'addaddress.html')
  return render(request,'landingpage.html')





def orderlist(request):
    if request.user.is_superuser:
        oc=oldcart.objects.all()
        return render(request,'orderlist.html',{'oc':oc})





def myorder(request):
    if request.user.is_authenticated:

        details=user_details.objects.get(user=request.user.id)
        orders=Order.objects.filter(user=details)
        cart2=oldcart.objects.filter(user=details)
        cart1 =reversed(list(cart2))

        return render(request,'myorder.html',{'details':details,'orders':orders,'cart1':cart1})
    return render(request,'login.html')




def ordercancel(request,id):
  if request.user.is_authenticated: 
    od_can=Order.objects.get(id=id)
    od_can.status='Cancelled'
    od_can.save()
    return redirect(myorder)

def orderreturn(request,id):
    if request.user.is_authenticated:
        od_rt=Order.objects.get(id=id)
        od_rt.status="Return"
        od_rt.save()
        return redirect(myorder)


def orderupdate(request,id):
    if request.user.is_superuser:
        if request.method == 'POST':
            stat=request.POST.get('stat')
            oc=oldcart.objects.get(order_id=id)
            oc.order.status=stat
            oc.order.save()
            return redirect(orderlist)



def orderplaced(request):
    return render(request,'placed.html')




def saleslist(request):
    if request.user.is_superuser:
        od=Order.objects.all()
        return render(request,'salesreport.html',{'od':od})


def date_select(request):
    start = request.POST['start_date']
    end = request.POST['end_date']
    if len(start) < 1 :
        messages.error(request,'Choose Start date')
        return redirect(saleslist)
    if len(end) < 1 :
        messages.error(request,'Choose End date')
        return redirect(saleslist)
    od = Order.objects.filter(order_date__range=[start,end])
    o_count = len(od)
    return render(request, 'salesreport.html',{'od':od,'o_count' : o_count})



def yearly_sales(request):
    year = request.POST['year']
    od = Order.objects.filter(order_date__year=year)
    o_count = len(od)   
    return render(request, 'salesreport.html',{'od':od,'o_count' : o_count})



def monthly_sales(request):
    month = request.POST['month']
    od = Order.objects.filter(order_date__month=month)
    o_count = len(od)
    return render(request, 'salesreport.html',{'od':od,'o_count' : o_count})



from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import FileResponse



def report(request):
    print(request.method)
    start = request.POST['start_date']
    end = request.POST['end_date']
    print("end=",end)
    order = Order.objects.filter(order_date__range=[start,end])
    print(order)
    n=len(order)
    print(n)
    if n==0:
        messages.error(request, 'No Order Found')
        return redirect('sales')
    print(order)
    type = request.POST['type']
    print(type)
    if type == 'PDF':
        
        template_path = 'report.html'

        context = {'order': order}

        response = HttpResponse(content_type='application/pdf')

        response['Content-Disposition'] = 'filename="invoice.pdf"'

        template = get_template(template_path)

        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response




def invoice(request,id):
    if request.user.is_authenticated:

        oc=oldcart.objects.get(order_id=id)
        template_path = 'orderinvoice.html'

        context = {'oc': oc}

        response = HttpResponse(content_type='application/pdf')

        response['Content-Disposition'] = 'filename=" Order invoice.pdf"'

        template = get_template(template_path)

        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response





def razorpay(request):
    cart = Cart.objects.filter(user=request.user.user_details)
    subtotal = 0
    for i in range(len(cart)):
        x = cart[i].product.price*cart[i].quantity
        subtotal = subtotal+x 
    total = subtotal
    return JsonResponse({
                         'total': total,})

