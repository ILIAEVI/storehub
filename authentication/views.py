from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def custom_logout(request):
    logout(request)
    return redirect('home')
