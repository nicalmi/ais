# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 08:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0013_auto_20180910_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruitmentapplication',
            name='exhibitor',
        ),
    ]