# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-04 09:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171003_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dias_aviso',
        ),
    ]
