from __future__ import unicode_literals
from ..lr_app.models import User
from django.db import models

# Create your models here.

class Description(models.Model):
    content = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    descripton = models.OneToOneField(Description, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    users = models.ManyToManyField(User, related_name='users')
