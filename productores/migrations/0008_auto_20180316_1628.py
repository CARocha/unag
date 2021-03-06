# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-16 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productores', '0007_encuesta_ronda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acuicola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posse', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=20, verbose_name='Posee')),
            ],
            options={
                'verbose_name_plural': 'Posee \xe1reas acu\xedcolas',
            },
        ),
        migrations.CreateModel(
            name='Apicola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colmenas', models.IntegerField(verbose_name='N\xfamero de colmenas')),
            ],
            options={
                'verbose_name_plural': 'Ap\xedcolas',
            },
        ),
        migrations.AlterModelOptions(
            name='produccionhuevosleche',
            options={'verbose_name_plural': 'Producci\xf3n de carne, huevos, leche, miel y otros'},
        ),
        migrations.AlterModelOptions(
            name='tierrasalquiladas',
            options={'verbose_name_plural': 'Posee tierras alquiladas'},
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='ronda',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V')]),
        ),
        migrations.AlterField(
            model_name='produccionhuevosleche',
            name='tipo_produccion',
            field=models.CharField(choices=[('Producci\xf3n de huevos por mes', 'Producci\xf3n de huevos por mes'), ('Producci\xf3n de leche (litros por d\xeda)', 'Producci\xf3n de leche (litros por d\xeda)'), ('Producci\xf3n de miel (kg/a\xf1o)', 'Producci\xf3n de miel (kg/a\xf1o)'), ('Producci\xf3n de carne (kg/a\xf1o)', 'Producci\xf3n de carne (kg/a\xf1o)'), ('Producci\xf3n de pez (kg/a\xf1o)', 'Producci\xf3n de pez (kg/a\xf1o)')], max_length=40),
        ),
        migrations.AddField(
            model_name='apicola',
            name='encuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productores.Encuesta'),
        ),
        migrations.AddField(
            model_name='acuicola',
            name='encuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productores.Encuesta'),
        ),
    ]
