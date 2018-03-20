# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-26 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0059_auto_20170926_2020'),
    ]

    database_operations = [
        migrations.AlterModelTable('BanquetteAttendant', 'banquet_banquetteattendant')
    ]

    state_operations = [
        migrations.DeleteModel(
            name='BanquetteAttendant',
        )
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]