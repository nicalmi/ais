# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0073_companycustomer_main_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='allow_status',
            field=models.BooleanField(default=False),
        ),
    ]
