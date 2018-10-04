# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-02 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_profile_kth_synchronize'),
        ('banquet', '0004_auto_20180910_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='dietary_preferences',
        ),
        migrations.AddField(
            model_name='participant',
            name='alcohol',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='dietary_restrictions',
            field=models.ManyToManyField(to='people.DietaryRestriction'),
        ),
    ]
