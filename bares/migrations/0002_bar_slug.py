# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]