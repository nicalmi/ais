# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-04 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_signupcontract_contract_company_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupcontract',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
