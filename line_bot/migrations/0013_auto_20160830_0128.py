# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0012_auto_20160830_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
