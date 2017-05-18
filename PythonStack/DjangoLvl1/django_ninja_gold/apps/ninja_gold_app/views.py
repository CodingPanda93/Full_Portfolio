from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    context = {
        'activities': request.session['activities']
    }
    # list of activities is reversed to show most recent activity at the top
    context['activities'].reverse()
    return render(request, 'ninja_gold/index.html', context)

def process_money(request, location):
    if request.method == 'POST':
        if location == 'farm':
            earning = random.randrange(10, 20)
            activity = 'Earned {} golds from the farm!'.format(earning)
            earning += request.session['gold']
            style = 'green'
        elif location == 'cave':
            earning = random.randrange(5,10)
            activity = 'Earned {} golds from the cave!'.format(earning)
            earning += request.session['gold']
            style = 'green'
        elif location == 'house':
            earning = random.randrange(2, 5)
            activity = 'Earned {} golds from the house!'.format(earning)
            earning += request.session['gold']
            style = 'green'
        elif location == 'casino':
            earning = random.randrange(0, 51)
            gamble = random.randint(0,1)

            if gamble == 0:
                activity = 'Earned {} golds from the house!'.format(earning)
                style = 'green'
            else:
                activity = 'Lost {} golds from the casino..Ouch!'.format(earning)
                earning = earning * -1
                style = 'red'
    else:
        return redirect('/')


    date = strftime("(%Y/%m/%d %I:%M %p)", gmtime()) #Did not import strftime or gmtime!!!!! CAUSES ERROR
    activity = activity + " " + date
    request.session['activities'].append([activity, style])


    return redirect('/')
