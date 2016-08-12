# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0008_auto_20160810_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='image',
        ),
    ]
