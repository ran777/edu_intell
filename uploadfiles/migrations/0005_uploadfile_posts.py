# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('uploadfiles', '0004_uploadfile_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='Posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Posts'),
        ),
    ]
