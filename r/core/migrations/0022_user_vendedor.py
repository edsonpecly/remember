# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-22 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20171016_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vendedor',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Vendedor Responsável'),
        ),
    ]
