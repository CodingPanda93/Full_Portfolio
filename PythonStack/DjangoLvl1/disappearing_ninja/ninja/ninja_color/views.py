from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'ninja/index.html')

def show_all(request):
    return render(request, 'ninja/all_ninja.html')

def show_ninja(request, ninja_color):
    if ninja_color == 'blue':
        ninja = 'Leonardo'
    elif ninja_color == 'orange':
        ninja = 'Michelangelo'
    elif ninja_color == 'red':
        ninja = 'Raphael'
    elif ninja_color == 'purple':
        ninja = 'Donatello'
    else:
        ninja = 'Megan'
    context = {
        'ninja_color': ninja
    }
    return render(request, 'ninja/ninja.html', context)
