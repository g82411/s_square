# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150716_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonsterPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('time', models.DateField(auto_now=True)),
                ('mid', models.ForeignKey(to='api.Monster')),
            ],
        ),
        migrations.CreateModel(
            name='UserPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('time', models.DateField(auto_now=True)),
                ('uid', models.ForeignKey(to='api.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='position',
            name='uid',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
