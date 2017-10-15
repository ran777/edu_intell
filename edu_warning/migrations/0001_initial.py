# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_auto_20171014_0419'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryWarning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('attachment', models.CharField(max_length=200)),
                ('edu_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.EduCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
