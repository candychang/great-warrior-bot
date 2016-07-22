# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0005_auto_20160701_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.TextField()),
                ('line_id', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(to='line_bot.UserModel', default=1),
            preserve_default=False,
        ),
    ]
