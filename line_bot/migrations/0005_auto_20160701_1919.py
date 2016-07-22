# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0004_auto_20160701_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='item',
            new_name='itemrequest',
        ),
    ]
