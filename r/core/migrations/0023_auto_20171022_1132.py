# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-22 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_user_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vendedor',
            field=models.CharField(blank=True, default='0', max_length=10, null=True, verbose_name='Vendedor Responsável'),
        ),
    ]
