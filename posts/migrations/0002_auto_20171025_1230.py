# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='click_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='download_num',
            field=models.IntegerField(default=0),
        ),
    ]
