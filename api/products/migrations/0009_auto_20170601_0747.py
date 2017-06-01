# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 07:47
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_component_background1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_link),
        ),
    ]