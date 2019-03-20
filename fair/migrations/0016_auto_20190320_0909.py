# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-20 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fair', '0015_auto_20190101_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fair',
            name='complete_registration_close_date',
            field=models.DateTimeField(default='2001-01-01 00:00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fair',
            name='complete_registration_start_date',
            field=models.DateTimeField(default='2001-01-01 00:00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fair',
            name='registration_end_date',
            field=models.DateTimeField(default='2001-01-01 00:00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fair',
            name='registration_start_date',
            field=models.DateTimeField(default='2001-01-01 00:00:00'),
            preserve_default=False,
        ),
    ]
