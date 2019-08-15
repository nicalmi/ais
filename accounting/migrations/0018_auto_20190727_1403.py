# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-27 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0017_auto_20181128_1141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'default_permissions': [], 'ordering': ['category', 'name'], 'permissions': [('base', 'View the Accounting tab'), ('export_orders', 'Export orders'), ('ths_customer_ids', 'Edit companies without THS customer IDs')], 'verbose_name_plural': 'Products'},
        ),
    ]
