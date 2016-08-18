# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0007_auto_20160722_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('ordered', models.TextField(default='')),
                ('issue', models.TextField(default='')),
                ('newOrder', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='cost',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='request',
            name='image',
            field=models.TextField(default=''),
        ),
    ]
