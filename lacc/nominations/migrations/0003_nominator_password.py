# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nominations', '0002_auto_20171104_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='nominator',
            name='password',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
