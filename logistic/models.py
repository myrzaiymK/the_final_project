from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Logistic(models.Model):
    name = models.CharField(max_length=200, blank=True)
    weight = models.IntegerField(blank=True)
    volume = models.IntegerField(blank=True, default=0)
    where_from = models.CharField(max_length=200, blank=True)
    where_to = models.CharField(max_length=200, blank=True)
    price = models.IntegerField()




# class HitCount(models.Model):
#     visits = models.IntegerField(default=0)

