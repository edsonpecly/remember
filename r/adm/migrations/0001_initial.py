# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-07 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitarPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(blank=True, max_length=50, null=True, verbose_name='Solicitante')),
                ('plano', models.CharField(blank=True, choices=[('1', 'Ouro - R$ 95,88/ano'), ('2', 'Prata - R$ 29,70/trimestre'), ('3', 'Bronze - R$ 11,99/mês ')], default='1', max_length=50, null=True, verbose_name='Plano Escolhido')),
                ('pagamento', models.CharField(blank=True, choices=[('1', 'Depósito Bancário'), ('2', 'Boleto')], default='1', max_length=50, null=True, verbose_name='Tipo de Pagamento')),
                ('status', models.CharField(blank=True, choices=[('1', 'Não Atendida'), ('2', 'Atendida')], default='1', max_length=30, null=True, verbose_name='Status Solicitação')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Solicitação de Pagamento',
                'verbose_name_plural': 'Solicitações de Pagamento',
            },
        ),
    ]
