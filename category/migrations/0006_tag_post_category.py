# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_auto_20171014_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='post_category',
            field=models.ManyToManyField(to='category.PostCategory'),
        ),
    ]