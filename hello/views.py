from django.http import request
from django.shortcuts import render, HttpResponse
from datetime import datetime
from hello.models import Contact, Login, Signup
from django.contrib import  messages

# Create your views here.
def index(request):
   return render(request, 'index.html')

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')

def fybsc(request):
    return render(request, 'fybsc.html')

def sybsc(request):
    return render(request, 'sybsc.html')

def login(request):
 if request.method == 'POST':
  username = request.POST.get('username')
  password = request.POST.get('password')

  login = Login(username=username, password=password, date=datetime.today())
  
  print(username.count())

  login.save()
  messages.success(request, 'You are Successfully Logged In')
 return render(request, 'login.html')

def signup(request):
 if request.method == 'POST':
  username = request.POST.get('username')
  password = request.POST.get('password')
  conferm_password = request.POST.get('conferm_password')
  email = request.POST.get('email')
  signup = Signup(username = username, password=password, conferm_password=conferm_password,email=email, date= datetime.today())
  signup.save()
  messages.success(request, 'Your Account has been Created')
 return render(request, 'signup.html')

def forgetpassword(request):
    return render(request, 'forgetpassword.html')
def contact(request):
    if request.method == 'POST':
     name = request.POST.get('name')
     email = request.POST.get('email')
     phone = request.POST.get('phone')
     desc = request.POST.get('desc')
     contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
     contact.save()
     messages.success(request, 'Your message has been sent.')

    return render(request, 'contact.html') 