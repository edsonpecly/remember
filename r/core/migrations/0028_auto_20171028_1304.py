# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20171028_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adm.Vendedor', verbose_name='Vendedor Responsável'),
        ),
    ]
