from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        'time': datetime.now().strftime('%I:%M %p'),
        'date': datetime.now().strftime('%b %d, %Y')
    }
    return render(request, 'timedisplay/index.html', context) #object, file path, dictionary
