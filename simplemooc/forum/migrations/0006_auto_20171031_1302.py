# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20171031_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='slug',
            field=models.SlugField(default='', max_length=100, verbose_name='Identificador'),
        ),
    ]
