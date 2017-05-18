from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]*$')

class EmailManager(models.Manager):
    def email_validation(self, postData):
        errors = []
        if len(postData['email']) < 2:
            errors.append('Email must be at least two characters!')
        if not re.match(EMAIL_REGEX, postData['email']):
            errors.append('This email is not a valid email address')
        if not errors:
            user = Email.objects.create(email=postData['email'])
        return errors

class Email(models.Model):
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    objects=EmailManager()

    #def __str__(self):
    #    return self.email
