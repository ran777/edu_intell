# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu_warning', '0003_auto_20171017_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionnaire',
            old_name='num',
            new_name='population',
        ),
    ]
