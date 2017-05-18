from __future__ import unicode_literals

from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\.\+_-]+\.[a-zA-Z]*$')
PASSWORDregex = re.compile(r'^(?=[^A-Z]*[A-Z])(?=[^0-9]*[0-9])[\w\d]{8,}$')

class UserManager(models.Manager):
    def register(self, postData):
        #verification variable
        error = []
        if len(postData['first_name']) < 1: #Validations for First Name
            error.append('First Name can not be empty!')
        elif not (postData['first_name'].isalpha()):
            error.append('First Name can not contain any numbers or special characters!')
        if len(postData['last_name']) < 1: #Validations for Last Name
            error.append('Last Name can not be empty!')
        elif not (postData['last_name']).isalpha():
            error.append('Last Name can not contain any numbers or special characters!')
        if len(postData['email']) < 1: #Validations for Emails
            error.append('Email can not be empty!')
        elif not EMAIL_REGEX.match(postData['email']):
            error.append("Invalid Email Address!")
        if len(postData['password']) < 1: #Validations for Password
            error.append('Password can not be empty!')
        elif PASSWORDregex.match(postData['password']):
            error.append('Password needs to be more than 8 characters!')
        elif postData['password'] != postData['confirm']:
            error.append('Your passwords do not match')
        if len(postData['confirm']) < 1: #Validations for Confirm Password
            error.append('You must confirm your password!')
            #Validation Statements: IF error holds a value it will return back to the main page and display flash messaging,
            # ELSE the information will be encrypted and saved to database
        if not error:
            # PASSED ALL VALIDATIONS: creating the password hash with bcrypt and earlier made variables
            hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=hashed_password,
            )
        return error

    def login(self, postData):
        #verification list
        error=[]
        if len(postData['email']) < 1: #Validations for Email
            error.append('Email can not be empty!')
        elif not EMAIL_REGEX.match(postData['email']):
            error.append("Invalid Email Address!")
        if len(postData['password']) < 1: #Validations for Password
            error.append('Password can not be empty!')
        elif PASSWORDregex.match(postData['password']):
            error.append('Password needs to be more than 8 characters!')
        user = User.objects.filter(email=postData['email'])
        if not user:
            return False
        if bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()) != user[0].password.encode():
            return False
        else:
            return user[0]


class User(models.Model):
      first_name = models.CharField(max_length=45)
      last_name = models.CharField(max_length=45)
      email = models.CharField(max_length=45)
      password = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      # *************************
      # Connect an instance of UserManager to our User model overwriting
      # the old hidden objects key with a new one with extra properties!!!
      objects = UserManager()
