# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0015_auto_20160830_0157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='cost_limit',
            new_name='budget',
        ),
    ]
