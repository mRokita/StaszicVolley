# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volley', '0002_auto_20170304_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score_a', models.IntegerField(verbose_name='Punkty zespo\u0142u A')),
                ('score_b', models.IntegerField(verbose_name='Punkty zespo\u0142u B')),
                ('team_a', models.ForeignKey(related_name='team_a', verbose_name='Zesp\xf3\u0142 A', to='volley.Team')),
                ('team_b', models.ForeignKey(related_name='team_b', verbose_name='Zesp\xf3\u0142 B', to='volley.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='school',
            field=models.CharField(default='liceum', max_length=10, verbose_name='Szko\u0142a', choices=[('liceum', 'Liceum'), ('gimnazjum', 'Gimnazjum')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='E-mail'),
            preserve_default=True,
        ),
    ]
