# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-07 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20171007_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pagamento',
            field=models.CharField(blank=True, choices=[('1', 'Depósito Bancário'), ('2', 'Boleto')], default='1', max_length=50, null=True, verbose_name='Tipo de Pagamento'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Não Atendida'), ('2', 'Atendida')], default='1', max_length=30, null=True, verbose_name='Status Solicitação'),
        ),
        migrations.AlterField(
            model_name='user',
            name='plano',
            field=models.CharField(blank=True, choices=[('1', 'Ouro - R$ 95,88/ano'), ('2', 'Prata - R$ 29,70/trimestre'), ('3', 'Bronze - R$ 11,99/mês ')], max_length=10, null=True, verbose_name='Plano'),
        ),
    ]
