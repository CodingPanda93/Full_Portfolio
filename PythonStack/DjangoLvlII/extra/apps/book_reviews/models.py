from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import User


class BookManager(models.Manager):

    def validate_new(self, postData, user_id):

        messages = []

        if postData['title'] == "":
            messages.append('Title cannot be blank')

        elif len(postData['title']) < 2:
            messages.append('Please enter a valid title')

        if postData['author'] == "" and postData['author_id'] == "":
            messages.append('Author can not be blank')

        elif postData['author_id'] == ""  and len(postData['author']) < 2:
            messages.append('Author cannot be blank')

        elif postData['author_id'] != "" and postData['author'] != "":
            messages.append('Please either choose an author from list or enter a new one')

        elif Author.objects.filter(name=postData['author']):
            messages.append('The author you entered is already part of the list')


        if postData['book_review'] == "":
            messages.append('Review cannot be blank')

        elif len(postData['book_review']) < 8:
            messages.append('Review must be at least 8 characters long')


        if len(messages) > 0:

            return (False, messages)

        else:

            new_book = self.add_book(postData, user_id)

            return (True, new_book)


    def get_author(self, postData):

        if postData['author'] != "":

            # add author to DB and return
            return Author.objects.create(name=postData['author'])

        else:

            # get author from DB and return
            return Author.objects.get(id=postData['author_id'])


    def add_book(self, postData, user_id):

        author = self.get_author(postData)
        book = Book.objects.create(title=postData['title'], author=author)
        user = User.objects.get(id=user_id)
        user_review = Review.objects.create(content=postData['book_review'], rating=postData['rating'], user=user, book=book)

        return book

    def add_review(self, postData, book_id, user_id):

        messages = []

        if postData['book_review'] == "" or len(postData['book_review']) < 8:
            messages.append('Review must be at least 8 characters')
            return (False, messages)

        else:

            user = User.objects.get(id=user_id)
            book = Book.objects.get(id=book_id)
            Review.objects.create(content=postData['book_review'], rating=postData['rating'], user=user, book=book)

            messages.append('Review successfuly added!')

            return (True, messages)


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    reviews = models.ManyToManyField(User, through="Review")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    content = models.CharField(max_length=1000)
    rating = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
