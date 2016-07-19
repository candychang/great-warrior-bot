# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
