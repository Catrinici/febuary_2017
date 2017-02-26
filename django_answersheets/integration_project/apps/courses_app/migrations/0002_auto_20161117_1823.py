# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='descripton',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses_app.Description'),
        ),
    ]
