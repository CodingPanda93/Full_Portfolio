from django.shortcuts import render, redirect

def index(request):
    return render(request, 'vinmyMVC/index.html')

def show(request):
    print request.method
    return render(request, 'vinmyMVC/index.html')

def create(request):
    print (request.method)
    if request.method=="POST":
        print ('*'*8)
        print (request.POST)
        request.session['name']=request.POST['name']
        return redirect('/')
    else:
        return redirect('/')
