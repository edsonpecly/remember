# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-21 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20171020_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='celular',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='Celular'),
        ),
    ]
