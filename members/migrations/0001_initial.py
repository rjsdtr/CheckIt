# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 18:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('tel_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(default=None, upload_to='profile/pic/%Y/%m/%d')),
                ('firsttime', models.BooleanField(default=True)),
                ('firstName', models.CharField(max_length=200, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=200, null=True, verbose_name='Last Name')),
                ('nickname', models.CharField(max_length=200, verbose_name='Nick name')),
                ('aim', models.CharField(max_length=200, verbose_name='Your ambition')),
                ('contact', models.CharField(blank=True, max_length=15, null=True)),
                ('resume', models.FileField(upload_to='profile/cv/%Y/%m/%d')),
                ('ranking', models.IntegerField(blank=True, default=0, null=True)),
                ('aboutme', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Country')),
                ('followers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('ranking',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField(blank=True, null=True)),
                ('location', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('certificate', models.FileField(upload_to='profile/projects/certificates/%Y/%m/%d')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('ranking', models.IntegerField()),
                ('profiles', models.ManyToManyField(to='members.Profile')),
            ],
            options={
                'ordering': ('ranking',),
            },
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, verbose_name='Skill Category')),
                ('ranking', models.IntegerField()),
            ],
            options={
                'ordering': ('ranking',),
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.SkillCategory'),
        ),
    ]
