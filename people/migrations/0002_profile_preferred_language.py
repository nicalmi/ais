# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-28 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='preferred_language',
            field=models.CharField(blank=True, choices=[('ENGLISH', 'English'), ('SWEDISH', 'Swedish')], max_length=255, null=True),
        ),
    ]
