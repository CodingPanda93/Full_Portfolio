from django.shortcuts import render, redirect
import random

#will not create word on refresh of screen
def index(request):
    if 'word' not in request.session:
        return redirect('/create_word')
    else:
        return render(request, 'random_word/index.html')

#define our session values: count and word
def create_word(request):
    #define/modify count when request is sent
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    #create new random word when request is sent
    word = ''
    charset = 'ABCDEFGHIJKLMNOPQRSTUVXYZ123456789'

    for i in range(14):
        word += random.choice(charset)

    request.session['word'] = word

    return redirect('/')
