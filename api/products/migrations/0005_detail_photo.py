# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170524_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='products/detail/photos/%Y/%m/%d'),
        ),
    ]