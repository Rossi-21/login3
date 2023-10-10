from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout

from .models import User
import bcrypt

def home(request): 
    return render(request, "index.html")



def registerUser(request):
        errors = User.objects.validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)

                return redirect('register')
            
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

            user = User.objects.create(
                 first_name = first_name, last_name = last_name, email = email, password = pw_hash
            )

        return render(request, "register.html", user)