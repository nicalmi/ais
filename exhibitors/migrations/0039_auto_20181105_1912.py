# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import exhibitors.models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0038_auto_20181105_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lunchticket',
            name='token',
            field=models.CharField(default=exhibitors.models.get_random_32_length_string, max_length=255, unique=True),
        ),
    ]
