# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-19 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='corta',
            field=models.IntegerField(),
        ),
    ]
