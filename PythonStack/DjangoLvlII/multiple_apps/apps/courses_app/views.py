from django.shortcuts import render, redirect, HttpResponse
from .models import Courses, Users

def index(request):
    context = {
    #shows all Courses available
        'courses': Courses.objects.all()
    }
    return render (request, 'courses_app/index.html', context)

def add(request):
    #creates new course from index.html then redirects to same page
    Courses.objects.create(number=request.POST['number'], name= request.POST['name'], description= request.POST['description'])
    return redirect ('courses:index')

def confirm_remove(request, id):
    context = {
        'course' : Courses.objects.get(id=id)
    }
    return render (request, 'courses_app/delete.html', context)

def destroy(request, id):
    Courses.objects.get(id=id).delete()
    return redirect('courses:index')

def add_user(request):
    context = {
    #shows all Courses available
        'courses': Courses.objects.all()
    }
    return render (request, 'courses_app/courses.html', context)
