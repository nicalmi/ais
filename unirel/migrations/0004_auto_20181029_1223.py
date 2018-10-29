# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unirel', '0003_participant_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='addon_banquet',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='participant',
            name='phone_number',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
