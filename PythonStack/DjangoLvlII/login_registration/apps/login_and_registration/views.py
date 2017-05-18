from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render (request, 'login_registration/index.html')

def register(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        error = User.objects.register(request.POST)
        if error:
            for error in error:
                messages.error(request, error)
                return redirect('/')
        else:
            messages.success(request, "Successfully registered (or logged in)!")
            return redirect('/success')

def login(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        user = User.objects.login(request.POST)
        if not user:
            messages.error(request, "Invalid Email and Password")
            return redirect('/')
        else:
            request.session['first_name'] = user.first_name
            messages.success(request, "Successfully register (or logged in)!")
            return redirect('/success')

def success(request):
    return render(request, 'login_registration/success.html')
