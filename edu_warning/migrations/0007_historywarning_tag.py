# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_remove_tag_post_category'),
        ('edu_warning', '0006_auto_20171014_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='historywarning',
            name='tag',
            field=models.ManyToManyField(to='category.Tag'),
        ),
    ]
