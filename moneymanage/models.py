from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class Sav_list(models.Model):
    description = models.TextField(default='')
    amount = models.IntegerField(default=0)
    sav_type = models.CharField(max_length=10)
    sav_time = models.DateTimeField(default=datetime.now)
    owner = models.TextField(default='')

class Gold_price(models.Model):
    buy_price = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)

class Stock(models.Model):
    stock_name = models.CharField(max_length=10)
    value = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    add_time = models.DateTimeField(default=datetime.now)

class Bank(models.Model):
    name = models.CharField(max_length=10)
    fixed_min = models.FloatField(default=0.0)
    fixed_max = models.FloatField(default=0.0)
    saving = models.FloatField(default=0.0)
    add_time = models.DateTimeField(default=datetime.now)
