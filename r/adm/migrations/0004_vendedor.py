# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0003_auto_20171019_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=14, verbose_name='Telefone')),
                ('comissao', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Comissao')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
                'ordering': ['nome', 'comissao'],
            },
        ),
    ]
