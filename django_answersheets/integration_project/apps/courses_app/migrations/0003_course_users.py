# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lr_app', '0001_initial'),
        ('courses_app', '0002_auto_20161117_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(related_name='users', to='lr_app.User'),
        ),
    ]