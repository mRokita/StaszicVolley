# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volley', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Activity',
            new_name='Post',
        ),
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='Zweryfikowany'),
            preserve_default=False,
        ),
    ]
