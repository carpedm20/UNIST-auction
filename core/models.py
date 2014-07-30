#-*- coding: utf-8 -*-
from django.db import models

from account.models import Account

# Create your models here.
class Stuff(models.Model):
    name = models.CharField(max_length=100)
    start_price = models.IntegerField()
    last_update = models.DateField(auto_now=True)
    img_url = models.URLField()
    detail = models.TextField()

    def __unicode__(self):
        return u"%s : %s원" % (name, price)

class Deal(models.Model):
    stuff = models.OneToOneField(Stuff)
    account = models.OneToOneField(Account)

    price = models.IntegerField()
    reason = models.TextField()

    def __uniocde__(self):
        return u"%s [%s] : ₩ %s" % (account, stuff, price)
