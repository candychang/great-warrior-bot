# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0014_auto_20160830_0134'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserModel',
            new_name='User',
        ),
    ]
