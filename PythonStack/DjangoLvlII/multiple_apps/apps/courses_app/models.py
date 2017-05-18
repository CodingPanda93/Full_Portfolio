from __future__ import unicode_literals

from django.db import models
from ..login_and_registration import User

class Courses(models.Model):
	number = models.IntegerField(max_value=500)
	name = models.CharField(max_length=50)
	students = models.ManyToManyField(User, related_name="attendance")
	description = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
