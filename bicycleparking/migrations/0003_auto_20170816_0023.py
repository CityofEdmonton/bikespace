# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-16 00:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bicycleparking', '0002_auto_20170815_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyanswer',
            old_name='comments',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='surveyanswer',
            name='photo_desc',
        ),
        migrations.RemoveField(
            model_name='surveyanswer',
            name='photo_uri',
        ),
    ]