from django.shortcuts import render, HttpResponse
from .models import User, Post

def index(request):
    context {
        user = User.objects.get(id=request.session['id'])
    }
