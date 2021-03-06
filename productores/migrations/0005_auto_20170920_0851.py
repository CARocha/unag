# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productores', '0004_auto_20170911_0845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otrastierras',
            options={'verbose_name_plural': '\xc1reas alquiladas de la finca (Mzs)'},
        ),
        migrations.AlterField(
            model_name='agricultura',
            name='tipo',
            field=models.CharField(choices=[('Cultivo de primera', 'Cultivo de primera'), ('Cultivo de postrera', 'Cultivo de postrera'), ('Cultivo de apante', 'Cultivo de apante'), ('Cultivos permanentes (Frutales, C\xedtricos, \u2026)', 'Cultivos permanentes (Frutales, C\xedtricos, \u2026)'), ('Otros', 'Otros')], max_length=50),
        ),
    ]
