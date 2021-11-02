from django.shortcuts import redirect, render
import random
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user, logout as logout_user, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Varify

@login_required(login_url='/profile/login/', redirect_field_name='/profile/')
def index(request):
    return render(request, 'profile/index.html')

def send_varification_mail(to_mail, otp, name):
    mail_from=settings.EMAIL_HOST_USER
    send_mail('Varification Mail', f'hello {name},\n Your OTP for varification is {otp}.', mail_from, to_mail)

def login(request):
    if request.user.is_authenticated == False:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login_user(request, user)
                return redirect('/profile/')
            else:
                return redirect('/profile/login/')
        else:
            return render(request, 'profile/login.html')
    else:
        return redirect('/profile/')

def signup(request):
    if request.user.is_authenticated == False:
        if request.method=='POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            user=User.objects.create_user(username, email, password)
            user.save()
            return redirect('/profile/login/')
        else:
            return render(request, 'profile/signup.html')
    else:
        return redirect('/profile/')

@login_required(login_url='/profile/login/')
def logout(request):
    logout_user(request)
    return redirect('/')
            