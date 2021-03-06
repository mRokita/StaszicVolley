# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volley', '0003_auto_20170412_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('title', models.CharField(max_length=128, verbose_name='Tytu\u0142')),
            ],
            options={
                'verbose_name': 'Turniej',
                'verbose_name_plural': 'Turnieje',
            },
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name': 'Mecz', 'verbose_name_plural': 'Mecze'},
        ),
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='volley.Tournament', verbose_name='Turniej'),
            preserve_default=False,
        ),
    ]
