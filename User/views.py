from django.shortcuts import render

from django.shortcuts import render, redirect

def home(request): 
    return render(request, "index.html")

def registerUser(request):
    return render(request, "register.html")