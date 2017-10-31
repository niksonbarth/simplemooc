# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 14:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='forum.Thread', verbose_name='Tópico'),
        ),
    ]