# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_warning', '0002_option_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
