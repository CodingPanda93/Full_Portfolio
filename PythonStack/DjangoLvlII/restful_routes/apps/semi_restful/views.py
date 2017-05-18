from django.shortcuts import render, redirect, reverse

from .models import Product

def index(request):
    context = {
    #shows all Products available
        'products': Product.objects.all()
    }
    return render (request, 'restful_routes/index.html', context)

def show(request, id):
    context = {
    #shows particular product for edit or deletion
        'product' : Product.objects.get(id=id)
    }
    return render (request, 'restful_routes/show.html', context)

def new(request):
    #shows form to create a new product
    return render (request, 'restful_routes/new.html')

def create(request):
    #creates new product from new.html then redirects to index.html
    Product.objects.create(name= request.POST['name'], description= request.POST['description'], price=request.POST['price'])
    return redirect (reverse('products:index'))

def edit(request, id):
    #shows product after being selected for editing
    context = {
        'product': Product.objects.get(id=id)
    }
    return render (request, 'restful_routes/edit.html', context)

def update(request, id):
    #updates/edits particular product when 'update' is selected
    product = Product.objects.update(id, request.POST)
    return redirect(reverse('products:index'), id=id)

def destroy(request, id):
    #deletes product listing when 'delete' is selected
    Product.objects.get(id=id).delete()
    return redirect(reverse('products:index'))
