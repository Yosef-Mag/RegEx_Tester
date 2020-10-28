from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(req):
    return render(req, 'appPages/dashboard.html') 

def logIn(req):
    if req.method == "POST":
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(req, 'appPages/login.html', {"form":form})    
    
    
def logOut(req):
    if req.method == 'POST':
        logout(req)
        return redirect('/')


def signUp(req):
    if req.method == "POST":
        form = SignUpForm(req.POST)
        if form.is_valid():
            user=form.save()
            login(req, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(req, 'appPages/signUp.html', {"form":form})

def profile(req):
    return HttpResponse('userProfile')