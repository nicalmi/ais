# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20181008_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='check_in_token',
            field=models.CharField(default='ILomjmwRGQ72LC4uyBychdPgxc7ebSYM', max_length=32, unique=True),
        ),
    ]
