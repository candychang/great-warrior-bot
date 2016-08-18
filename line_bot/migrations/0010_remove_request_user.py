# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0009_remove_request_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='user',
        ),
    ]
