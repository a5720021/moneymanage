from __future__ import unicode_literals

from django.db import models

class Sav_list(models.Model):
    description = models.TextField(default='')
    amount = models.IntegerField(default=0)
    sav_type = models.CharField(max_length=10)
    sav_time = models.DateTimeField(auto_now=True)

class Gold_price(models.Model):
    buy_price = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
    add_time = models.DateTimeField(auto_now=True)

class Stock(models.Model):
    name = models.CharField(max_length=10)
    value = models.FloatField(default=0.0)
    change = models.FloatField(default=0.0)
    add_time = models.DateTimeField(auto_now=True)

class Bank(models.Model):
    name = models.CharField(max_length=10)
    fixed = models.FloatField(default=0.0)
    saving = models.FloatField(default=0.0)
    add_time = models.DateTimeField(auto_now=True)
