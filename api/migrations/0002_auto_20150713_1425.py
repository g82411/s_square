# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('time', models.DateField(auto_now=True)),
                ('uid', models.ForeignKey(to='api.User')),
            ],
        ),
        migrations.AddField(
            model_name='box',
            name='monster',
            field=models.ForeignKey(default=1, to='api.Monster'),
            preserve_default=False,
        ),
    ]
