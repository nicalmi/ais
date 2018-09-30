# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-22 15:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0011_auto_20180815_1123'),
        ('fair', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fair',
            name='product_lunch_ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.Product'),
        ),
    ]