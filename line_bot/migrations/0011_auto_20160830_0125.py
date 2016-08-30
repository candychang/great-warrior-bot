# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0010_remove_request_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='itemrequest',
            new_name='item',
        ),
        migrations.RemoveField(
            model_name='request',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='request',
            name='itemcolor',
        ),
        migrations.RemoveField(
            model_name='request',
            name='size',
        ),
        migrations.AddField(
            model_name='request',
            name='cost_limit',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='request',
            name='details',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='request',
            name='quantity',
            field=models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(to='line_bot.UserModel', default=1),
        ),
    ]
