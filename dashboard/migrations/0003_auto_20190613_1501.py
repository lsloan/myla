# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-13 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_user_enrollment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseviewoption',
            name='course',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Course View Option Id'),
        ),
    ]
