# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-22 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0004_auto_20171022_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendaproduto',
            name='nova_compra',
            field=models.DateField(blank=True, null=True, verbose_name='Nova Compra'),
        ),
        migrations.AlterField(
            model_name='vendaproduto',
            name='retorno',
            field=models.DateField(blank=True, null=True, verbose_name='retorno'),
        ),
    ]
