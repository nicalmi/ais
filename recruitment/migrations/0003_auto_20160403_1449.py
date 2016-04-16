# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_group_is_role'),
        ('recruitment', '0002_roleforrecruitmentperiod'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitableRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruitment_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.RecruitmentPeriod')),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.RemoveField(
            model_name='roleforrecruitmentperiod',
            name='recruitment_period',
        ),
        migrations.RemoveField(
            model_name='roleforrecruitmentperiod',
            name='role',
        ),
        migrations.DeleteModel(
            name='RoleForRecruitmentPeriod',
        ),
    ]
