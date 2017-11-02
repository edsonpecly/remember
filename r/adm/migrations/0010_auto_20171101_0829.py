# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-01 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0009_auto_20171031_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='tipo_conta',
            field=models.CharField(blank=True, choices=[('1', 'Conta Poupança'), ('2', 'Conta Corrente')], max_length=50, null=True, verbose_name='Tipo da Conta'),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='conta',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='N° da Conta'),
        ),
    ]
