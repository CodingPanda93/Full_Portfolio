from django.shortcuts import render, redirect

#display our form on index page
def index(request):
    return render(request, 'survey_form/index.html')

def process(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    request.session['name']=request.POST['name']
    request.session['comment']= request.POST['comment']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    return redirect ('/result')

def result(request):
    return render (request, 'survey_form/result.html')
