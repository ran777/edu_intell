# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_warning', '0002_delete_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historywarning',
            name='attachment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='historywarning',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
