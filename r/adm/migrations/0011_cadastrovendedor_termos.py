# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-01 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0010_auto_20171101_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrovendedor',
            name='termos',
            field=models.BooleanField(default=False, verbose_name='Concordancia com os termos'),
        ),
    ]
