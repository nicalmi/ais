# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-15 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_registrationsection_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost_center',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='result_center',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]