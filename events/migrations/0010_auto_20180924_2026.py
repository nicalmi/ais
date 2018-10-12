# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-24 18:26
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20180923_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupquestion',
            name='options',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=[], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signupquestionanswer',
            name='answer_options',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=[], size=None),
            preserve_default=False,
        ),
    ]