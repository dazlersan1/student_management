from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import loginForm
from django.contrib import messages
from django.contrib.auth.models import User,auth


def login(request):
    if(request.user.is_authenticated):
        return redirect('/profile')
        
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = auth.authenticate(username = username, password = password)
        if(user is not None):
            auth.login(request,user)
            return redirect('/profile')
        else:
            messages.error(request,"Invalid username / password ")
            return render(request,'login.html')
    return render(request,'login.html')

def home(request):
    if(request.user.is_authenticated):
        print(request.user.username)
        return render(request,'index.html')
    else:
        return redirect("/login")
    
def logout(request):
    auth.logout(request)
    return redirect('/login')


def reset(request):
    return redirect('/reset_password')
