# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20171014_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcategory',
            name='parent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
