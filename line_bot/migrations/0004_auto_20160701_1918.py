# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0003_auto_20160701_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='color',
            new_name='itemcolor',
        ),
    ]
