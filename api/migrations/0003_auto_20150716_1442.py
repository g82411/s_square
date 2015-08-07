# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150713_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('friend_1', models.ForeignKey(related_name='friend_1', to='api.User')),
                ('owner', models.ForeignKey(related_name='owner', to='api.User')),
            ],
        ),
        migrations.AddField(
            model_name='position',
            name='target',
            field=models.CharField(default=b'User', max_length=32),
        ),
    ]
