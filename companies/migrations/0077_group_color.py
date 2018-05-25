# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0076_auto_20180524_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='color',
            field=models.CharField(blank=True, choices=[('BLUE', 'Blue'), ('RED', 'Red'), ('GREEN', 'Green'), ('YELLOW', 'Yellow')], max_length=200, null=True),
        ),
    ]
