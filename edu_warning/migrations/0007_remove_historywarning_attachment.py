# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu_warning', '0006_auto_20171022_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historywarning',
            name='attachment',
        ),
    ]