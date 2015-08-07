# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150716_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friend_1',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
