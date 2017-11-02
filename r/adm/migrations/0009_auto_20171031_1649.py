# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-31 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0008_auto_20171031_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='InserirComissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cliente')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Valor da Comissão')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Comissão',
                'verbose_name_plural': 'Comissões',
                'ordering': ['vendedor', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PagarComissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendedor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Vendedor')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Valor Pago')),
                ('status', models.CharField(blank=True, choices=[('1', 'Aguardando'), ('2', 'Pago')], default='1', max_length=20, null=True, verbose_name='Status da Solicitação')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Silicitação de Comissão',
                'verbose_name_plural': 'Solicitações de Comissões',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='cadastrovendedor',
            name='mensagem',
            field=models.TextField(blank=True, null=True, verbose_name='Mensagem'),
        ),
        migrations.AddField(
            model_name='vendedor',
            name='agencia',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Agencia'),
        ),
        migrations.AddField(
            model_name='vendedor',
            name='banco',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Banco'),
        ),
        migrations.AddField(
            model_name='vendedor',
            name='conta',
            field=models.CharField(blank=True, choices=[('1', 'Conta Poupança'), ('2', 'Conta Corrente')], max_length=50, null=True, verbose_name='N° da Conta'),
        ),
        migrations.AddField(
            model_name='inserircomissao',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adm.Vendedor', verbose_name='Vendedor'),
        ),
    ]