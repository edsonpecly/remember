# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-11 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20171010_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status_atendimento',
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='p_celular',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='2', max_length=5, verbose_name='Prof - Exibir Celular?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='p_data_nascimento',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='2', max_length=5, verbose_name='Prof - Exibir Data de Nascimento?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='p_endereco',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='2', max_length=5, verbose_name='Prof - Exibir Endereço?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='p_observacao',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='2', max_length=5, verbose_name='Prof - Exibir Observação?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='pr_custo',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='2', max_length=5, verbose_name='Prod - Exibir Custo?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='pr_observacao',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='2', max_length=5, verbose_name='Prod - Exibir Observação?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='pr_valor',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='1', max_length=5, verbose_name='Prod - Exibir Valor?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='s_observacao',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='2', max_length=5, verbose_name='Ser - Exibir Observação?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='s_valor',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='1', max_length=5, verbose_name='Ser - Exibir Valor?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='u_data_nascimento',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='2', max_length=5, verbose_name='Usu - Exibir Data de Nascimento?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='u_endereco',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='2', max_length=5, verbose_name='Usu - Exibir Endereço?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='u_observacao',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='2', max_length=5, verbose_name='Usu - Exibir Observação?'),
        ),
        migrations.AlterField(
            model_name='controlecadastro',
            name='u_telefone',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], default='2', max_length=5, verbose_name='Usu - Exibir Telefone?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tipo_pagamento',
            field=models.CharField(blank=True, choices=[('1', 'Depósito Bancário'), ('2', 'Boleto'), ('3', 'Cartão de Crédito')], default=3, max_length=50, null=True, verbose_name='Tipo de Pagamento'),
        ),
    ]
