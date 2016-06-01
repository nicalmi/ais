# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fair', '0002_fair_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fair',
            name='name',
            field=models.CharField(default='Armada 2016', max_length=100),
        ),
        migrations.AlterField(
            model_name='fair',
            name='year',
            field=models.IntegerField(default=2016),
        ),
    ]
