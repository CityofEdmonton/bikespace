# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-16 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicycleparking', '0003_auto_20170816_0023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyanswer',
            old_name='comment',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='surveyanswer',
            old_name='timestamp',
            new_name='point_timestamp',
        ),
        migrations.AddField(
            model_name='surveyanswer',
            name='photo_desc',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='surveyanswer',
            name='photo_uri',
            field=models.TextField(default=None),
        ),
    ]
