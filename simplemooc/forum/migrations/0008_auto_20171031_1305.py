# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20171031_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='forum.Thread', verbose_name='Tópico'),
        ),
    ]
