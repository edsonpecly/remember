# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-31 16:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20171030_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário só pode  conter letras, números ou os seguintes caracteres @/./+/-/_ Não pode conter espaço no username', 'invalid')], verbose_name='Nome de Usuário'),
        ),
    ]