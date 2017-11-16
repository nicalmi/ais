# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0010_remove_profile_portrait'),
        ('companies', '0025_auto_20170410_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='related_programme',
            field=models.ManyToManyField(blank=True, to='people.Programme'),
        ),
    ]
