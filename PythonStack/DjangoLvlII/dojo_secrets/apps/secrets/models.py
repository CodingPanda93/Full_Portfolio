from __future__ import unicode_literals

from django.db import models
from ..login_and_registration.models import User, UserManager

class Post(models.Model):
    post = models.CharField(max_length=1000)
    like_count = models.IntegerField()
    user = models.ForeignKey(User, related_name='poster')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
