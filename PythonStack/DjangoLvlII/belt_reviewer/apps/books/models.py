from __future__ import unicode_literals

from django.db import models
from ..login_and_registration.models import User
from django.core.validators import MaxValueValidator

class BookManager(models.Manager):
    def add_book(self, postData, user_id):
        #verfication variables
        error = []
        if len(postData['book_title']) < 1: #Validations for Book Title
            error.append('Book Title can not be empty!')
        #Validation Statements: IF error holds a value it will return back to the main page and display flash messaging,
        # ELSE the information will be saved to database
        if not error:
            book = Book.objects.create(
                title=postData['book_title'],
                author=self.get_author(postData)
            )
            review = self.add_review(postData, user_id, book.id)
        else:
            return error

    def add_review(self, postData, user_id, book_id):
        print type(user_id)
        user = User.objects.get(id=user_id)
        book = Book.objects.get(id=book_id)
        review = Review.objects.create(review=postData['review'], rating=postData['rating'], user=user, book=book)
        return review


    def get_author(self, postData):
        if len(postData['new_author']) < 1:
            author = Author.objects.get(id=postData['author_list'])
            return author
        else:
            author = Author.objects.create(name=postData['new_author'])
            return author

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    reviews = models.ManyToManyField(User, through='Review')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

    def __str__(self):
        return self.title

class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review
