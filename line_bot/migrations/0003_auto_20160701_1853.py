# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot', '0002_form_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('item', models.TextField(default='')),
                ('url', models.TextField(default='')),
                ('size', models.TextField(default='')),
                ('color', models.TextField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='Form',
        ),
    ]
