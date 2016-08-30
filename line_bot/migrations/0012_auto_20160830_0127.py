# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0011_auto_20160830_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='cost_limit',
            field=models.TextField(default=''),
        ),
    ]
