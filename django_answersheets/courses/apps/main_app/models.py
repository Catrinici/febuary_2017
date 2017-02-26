from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Description(models.Model):
    content = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    descripton = models.OneToOneField(Description, on_delete = models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
