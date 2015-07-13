# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('bid', models.AutoField(serialize=False, primary_key=True)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('mid', models.AutoField(serialize=False, primary_key=True)),
                ('mname', models.CharField(max_length=128)),
                ('initHP', models.IntegerField()),
                ('initAtk', models.IntegerField()),
                ('groHP', models.FloatField()),
                ('groAtk', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fir', models.ForeignKey(related_name='first', to='api.Box')),
                ('fou', models.ForeignKey(related_name='fourth', to='api.Box')),
                ('sec', models.ForeignKey(related_name='second', to='api.Box')),
                ('thi', models.ForeignKey(related_name='third', to='api.Box')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('sid', models.AutoField(serialize=False, primary_key=True)),
                ('target', models.CharField(max_length=40)),
                ('function', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(serialize=False, primary_key=True)),
                ('uname', models.CharField(max_length=128)),
                ('session', models.CharField(unique=True, max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='party',
            name='uid',
            field=models.ForeignKey(to='api.User'),
        ),
        migrations.AddField(
            model_name='box',
            name='owner',
            field=models.ForeignKey(to='api.User'),
        ),
    ]
