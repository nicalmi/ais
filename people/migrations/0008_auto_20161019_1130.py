# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-19 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import lib.image


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20160910_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to=lib.image.UploadToDir('profiles', 'picture')),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture_original',
            field=models.ImageField(blank=True, upload_to=lib.image.UploadToDirUUID('profiles', 'picture_original')),
        ),
    ]