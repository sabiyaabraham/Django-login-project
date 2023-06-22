from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

#Method for create a new User
def create_user(request):
    context = {
        "form": UserCreationForm
    }
    if request.method == "GET" :
        return render(request, "login.html", context)
    else:
        password = request.POST.get("password1")
        password_2 = request.POST.get("password2")
        username = request.POST.get("username")
        if password == password_2:
            try:
                user = User.objects.create_user(
                    username = username,
                    password = password,
                )
                user.save()
                login(request,user)
                return render(request, "home.html")
            except IntegrityError:
                messages.error(request, "The User is registered")
                return render(request, "login.html")
        else:
            messages.error(request, "Passwords must be the same")
            return render(request, "login.html")
        
#LogIn Method
def signin(request):
    context = {
        "form": AuthenticationForm
    }
    if request.method == 'GET':
        return render(request, "login.html", context)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, "Username or password is incorrect")
            return redirect('login')
        login(request, user)
        return render(request, "home.html")
    
#close session method
def close_session(request):
    logout(request)
    context = {
        "form": UserCreationForm
    }
    return render(request, "login.html", context)

def home(request):
    return render(request, "home.html")