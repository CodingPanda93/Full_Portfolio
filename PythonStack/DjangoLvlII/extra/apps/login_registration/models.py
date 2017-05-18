from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def validate_registration(self, postData):

        messages = []

        if postData['name'] == "":
            messages.append(('Name cannot be blank', 'name'))
        elif len(postData['name']) < 2:
            messages.append(('Please enter a valid name', 'name'))

        if postData['alias'] == "":
            messages.append(('Alias cannot be blank', 'alias'))
        elif len(postData['alias']) < 2:
            messages.append(('Please enter a valid alias with at least 2 characters', 'alias'))

        if postData['email'] == "":
            messages.append(('Email cannot be blank', 'email'))
        elif not re.match(email_regex, postData['email']):
            messages.append(('Please enter a valid email', 'email'))
        elif User.objects.filter(email=postData['email']):
            messages.append(('That email already in use', 'email'))

        if postData['password'] == "":
            messages.append(('Password cannot be blank and should be at least 8 characters', 'password'))
        elif len(postData['password']) < 8:
            messages.append(('Password must be at least 8 characters', 'password'))
        elif postData['password'] != postData['confirm_password']:
            messages.append(('Passwords must match', 'confirm_password'))

        if len(messages) > 0:
            return (False, messages)

        else:
            new_user = self.add_user(postData)

            user = {

                'id': new_user.id,
                'name': new_user.name,
                'alias': new_user.alias,
                'email': new_user.email
            }

            return (True, user)

    def add_user(self, postData):

        hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

        new_user = User.objects.create(name=postData['name'], alias=postData['alias'], email=postData['email'], password=hashed_pw)

        return new_user

    def validate_login(self, postData):

        messages = []

        if postData['email'] == "" or not re.match(email_regex, postData['email']) or len(postData['password']) < 8 or not User.objects.filter(email=postData['email']):

            messages.append('Invalid login')

            return (False, messages)


        login_user = User.objects.filter(email=postData['email'])

        if not bcrypt.hashpw(postData['password'].encode(), login_user[0].password.encode()) == login_user[0].password.encode():
            messages.append('Invalid login')

            return (False, messages)

        else:

            user = {

                'id': login_user[0].id,
                'name': login_user[0].name,
                'alias': login_user[0].alias,
                'email': login_user[0].email
            }

            return (True, user)


class User(models.Model):

    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
