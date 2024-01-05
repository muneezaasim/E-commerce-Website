from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import orders
import re

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def winter(request):
    return render(request, 'winter.html')


def confirmorder(request):
    latest_order = orders.objects.order_by('-orderID').first()
    return render(request, 'confirmorder.html', {'latest_order': latest_order})

def newin(request):
    return render(request, 'newin.html')

def productpage(request):
    return render(request, 'productpage.html' )

def productpage2(request):
    return render(request, 'productpage2.html' )

def productpage3(request):
    return render(request, 'productpage3.html' )

def productpage4(request):
    return render(request, 'productpage4.html' )
def shipping(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        zip = request.POST['zip']
        shipping_method = request.POST['shipping-method']
        payment_option = request.POST['payment-option']
        
        shipping_info = orders(
            name=name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            zip=zip,
            shipping_method=shipping_method,
            payment_option = payment_option
        )
        
        shipping_info.save()
      
        return redirect('confirmorder')
       
      # Redirect to a success page or another view
    else:
        return render(request, 'shipping.html')
        
def contactus(request):
    return render(request,'contactus.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def is_valid_email(email):
    # Define a regex pattern for a valid email format
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    # Check if the provided email matches the pattern
    return bool(re.match(email_pattern, email))

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        if not is_valid_email(email):
            messages.error(request, 'Invalid email format. Please provide a valid email address.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.info(request,"Email ALready exists")
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username already exists')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save();
            return redirect('register')
    else:    
        return render(request,'register.html')
    
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
       
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')  
    else:
        return render(request,'login.html')



# def counter(request):
#     text= request.POST['text']
#     amount_of_words = len(text.split())
#     return render(request, 'counter.html',{'amount': amount_of_words})