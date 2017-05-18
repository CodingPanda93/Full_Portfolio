from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User
from ..book_reviews.models import Review

#shows main login screen is said user is not already in session
def index(request):
    if 'user' in request.session:
        return redirect('book_reviews:index')
    else:
        return render(request, 'login_registration:index')

#Register user directs to validation within models and records if any error messages return IF NOT saves all data for user within sessions and continues
def create(request):

    if request.method != 'POST':
        return redirect('login_registration:index')

    else:
        response = User.objects.validate_registration(request.POST)
        if response[0] == False:
            for message in response[1]:
                messages.error(request, '*' + message[0], extra_tags=message[1])
            return redirect('login_registration:index')
        else:
            request.session['user'] = {
                'id': response[1]['id'],
                'name': response[1]['name'],
                'alias': response[1]['alias'],
                'email': response[1]['email']
            }


        return redirect('login_registration:index')

#Login user directs to validation within models and records if any error messages return IF NOT saves all data for user within sessions and continues
def login(request):
    if request.method != 'POST':
        return redirect('login_registration:index')
    else:
        response = User.objects.validate_login(request.POST)
        if response[0] == False:
            for message in response[1]:
                messages.error(request, '*' + message, 'login')
                return redirect('login_registration:index')
        else:
            request.session['user'] = {
                'id': response[1]['id'],
                'name': response[1]['name'],
                'alias': response[1]['alias'],
                'email': response[1]['email']
            }
            return redirect('login_registration:index')

#eliminates user from session to set back to index and wont auto-login
def logout(request):
    request.session.clear()
    return redirect('login_registration:index')


def user_reviews(request, id):
    try:
        user = User.objects.get(id=id)
        context = {
            'user': {
                'name': user.name,
                'alias': user.alias,
                'email': user.email,
            },
            'user_reviews': Review.objects.filter(user=user).order_by('book__title'),
            'count_reviews': Review.objects.filter(user=user).count()
        }

        return render(request, 'login_registration/user_reviews.html', context)
    #if user ID is not available will redirect to book reviews index
    except:
        return redirect('book_reviews:index')
