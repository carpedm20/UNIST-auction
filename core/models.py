#-*- coding: utf-8 -*-
from django.db import models

from account.models import Account

# Create your models here.
class Stuff(models.Model):
    name = models.CharField(max_length=100)
    start_price = models.IntegerField()
    min_diff_price = models.IntegerField()
    last_update = models.DateField(auto_now=True)
    img_url = models.URLField()
    detail = models.TextField()

    def __unicode__(self):
        return u"%s : %s원" % (name, price)

    @property
    def recent_price(self):
        if self.deal_set.count() == 0:
            return self.start_price
        else:
            max = 0
            for deal in self.deal_set.all():
                if deal.price > max:
                    max = deal.price
            return max

class Deal(models.Model):
    stuff = models.ForeignKey(Stuff)
    account = models.OneToOneField(Account)

    price = models.IntegerField()
    reason = models.TextField()
    is_name_filter = models.BooleanField()

    def __uniocde__(self):
        return u"%s [%s] : %s원" % (account, stuff, price)

    def save(self, *args, **kwargs):
        deal_count = self.stuff.deal_set.count()

        recent_deal = self.stuff.deal_set.all()[deal_count - 1]

        if self.price > recent_deal.price + self.stuff.min_diff_price:
            super(Deal, self).save(*args, **kwargs)
        else:
            msg = "오류: 불가능한 가격입니다."
            raise Exception(msg)
