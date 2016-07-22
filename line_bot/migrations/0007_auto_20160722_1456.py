# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0006_auto_20160722_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.ForeignKey(to='line_bot.UserModel', default=1),
        ),
    ]
