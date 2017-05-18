from django.shortcuts import render

def index(request):
    context = {
        "email": "mike@gmail.com",
        "name": "Mark"
    }
    return render(request, 'secondapp/index.html', context)

def show(request, id):
    context = {
        "id": id
    }
    return render(request, 'secondapp/index.html', context)
