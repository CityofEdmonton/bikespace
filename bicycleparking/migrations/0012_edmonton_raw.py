# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-23 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicycleparking', '0011_auto_20180831_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edmonton_Raw',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.BigIntegerField(blank=True, null=True)),
                ('endpoint_id', models.BigIntegerField(blank=True, null=True)),
                ('on_street_name_full_parent', models.CharField(blank=True, max_length=250, null=True)),
                ('at_street_name_full_parent', models.CharField(blank=True, max_length=250, null=True)),
                ('on_street_name_full', models.CharField(blank=True, max_length=250, null=True)),
                ('at_street_name_full', models.CharField(blank=True, max_length=250, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('the_geom', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'edmonton_raw',
                'managed': False,
            },
        ),
    ]
