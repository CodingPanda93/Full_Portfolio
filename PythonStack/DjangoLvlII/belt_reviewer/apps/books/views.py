from django.shortcuts import render, redirect, reverse
from .models import User, Book, Review, Author
from django.contrib import messages
import types

def index(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'recent_reviews': Review.objects.all().order_by('-created_at')[:3], #Recent 3 reviews ordered by created_at up to 3 reviews
        'all_books': Book.objects.all().order_by('title') #Setting up all book reviews ordered by titles
        }
    return render(request, 'books/index.html', context)
#shows selected book when selected on index page
def show_book(request, id):
    book = Book.objects.get(id=id)
    user=User.objects.get(id=request.session['user_id'])
    context = {
        'book' : book,
        'reviews': Review.objects.filter(book=book).order_by('-created_at')
    }
    return render(request, 'books/show_book.html', context)

#shows selected user to view requests entered
def show_user(request):
    pass

def new(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'books/new.html', context)

def create_book(request, id):
    if request.method != 'POST':
        return redirect('books:new')
    else:
        book = Book.objects.add_book(request.POST, id, request.session['user_id'])
        if isinstance(book, types.ListType):
            for error in book:
                messages.error(request, error)
                return redirect(reverse('books:show_book', id=id))
        else:
            messages.success(request, "Successfully added new book and review!")
            return redirect(reverse('books:show_book', id=id))

def create_review(request, id):
    if request.method != 'POST':
        return redirect('books:show_book', id=id)
    else:
        review = Book.objects.add_review(request.POST, id, request.session['user_id'])
        if isinstance(review, types.ListType):
            for error in review:
                messages.error(request, error)
                return redirect('books:show_book', id=id)
        else:
            messages.success(request, "Successfully added a review!")
            return redirect('books:show_book', id=id)

def update(request):
    pass

def destroy(request):
    pass
