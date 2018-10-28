# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banquet', '0013_auto_20181028_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invitation',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='banquet.InvitationGroup'),
            preserve_default=False,
        ),
    ]
