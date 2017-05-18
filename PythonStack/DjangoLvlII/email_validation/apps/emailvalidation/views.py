from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Email

def index(request):
    return render(request, 'email_validation/index.html')

def process(request):
    if request.method == 'POST':
        errors = Email.objects.email_validation(request.POST)
        if errors:
            for err in errors:
                messages.error(request, err)
            return redirect('/')
        else:
            messages.success(request, "The email address you entered {} is a VALID email address! Thank you!" .format(email.email))
            return redirect('/show')
    else:
        return redirect('/')

def show(request):
    context = {
        'emails': Email.objects.all().order_by('-created_at')
    }
    return render(request, 'email_validation/success.html', context)
