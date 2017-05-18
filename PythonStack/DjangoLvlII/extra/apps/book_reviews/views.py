from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author, Review
from ..login_registration.models import User

def index(request):
    # main page shows the 3 most recent book reviews and all existing books that have reviews
    if 'user' not in request.session:

        return redirect('login_registration:index')

    else:

        context = {

            'recent_reviews': Review.objects.all().order_by('-created_at')[:3],
            'all_books': Book.objects.all().order_by('title')

        }

        return render(request, 'book_reviews/index.html', context)


def add_book(request):

    if 'user' not in request.session:

        return redirect('login_registration:index')

    else:

        context = {

            'authors': Author.objects.all().order_by('name')

        }

        return render(request, 'book_reviews/add.html', context)

def create(request):

    if 'user' not in request.session or request.method != 'POST':

        return redirect('login_registration:index')

    else:

        response = Book.objects.validate_new(request.POST, request.session['user']['id'])

        if response[0] == False:

            for message in response[1]:

                messages.error(request, message)

            return redirect('book_reviews:add_book')

        else:

            book_id = response[1].id

            return redirect('book_reviews:show_book', id=book_id)


def show_book(request, id):

    if 'user' not in request.session:

        return redirect('login_registration:index')


    else:

        users = User.objects.all()

        try:

            book = Book.objects.get(id=id)

            context = {

                'book': book,
                'reviews': Review.objects.filter(book=book).order_by('-created_at')

            }

            return render(request, 'book_reviews/book.html', context)

        except:

            return redirect('book_reviews:index')


def add_review(request, id):

    if 'user' not in request.session:

        return redirect('login_registration:index')

    else:

        response = Book.objects.add_review(request.POST, id, request.session['user']['id'])

        if response[0] == False:

            for message in response[1]:

                messages.error(request, message)

        else:

            for message in response[1]:

                messages.success(request, message)

        return redirect('book_reviews:show_book', id=id)


def destroy_review(request, id, review_id):

    Review.objects.get(id=review_id).delete()

    return redirect('book_reviews:show_book', id=id)
