# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneymanage', '0002_gold_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('value', models.FloatField(default=0.0)),
                ('change', models.FloatField(default=0.0)),
                ('add_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
