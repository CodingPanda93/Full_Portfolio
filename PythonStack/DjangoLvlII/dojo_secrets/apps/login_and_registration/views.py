from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render (request, 'login_registration/index.html')

def register(request):
    if request.method != 'POST':
        return redirect('login_registration:index')
    else:
        error = User.objects.register(request.POST)
        if error:
            for error in error:
                messages.error(request, error)
                return redirect('login_registration:index')
        else:
            messages.success(request, "Successfully registered (or logged in)!")
            return redirect('secrets:index')

def login(request):
    if request.method != 'POST':
        return redirect('login_registration:index')
    else:
        user = User.objects.login(request.POST)
        if not user:
            messages.error(request, "Invalid Email and Password")
            return redirect('login_registration:index')
        else:
            request.session['id'] = user.id
            messages.success(request, "Successfully register (or logged in)!")
            return redirect('secrets:index')

def success(request):
    return render(request, 'login_registration/success.html')
