# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.AlterField(
            model_name='course',
            name='descripton',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main_app.Description'),
        ),
    ]
