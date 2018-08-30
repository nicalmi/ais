# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-30 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0010_auto_20180830_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='recruitment_period',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='recruitment.RecruitmentPeriod'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recruitmentapplication',
            name='slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruitment.Slot', verbose_name='Time and location'),
        ),
    ]