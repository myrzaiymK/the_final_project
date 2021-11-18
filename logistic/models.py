from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum,F
from django.urls import reverse
from django.db.models.fields import SlugField

class Logistic(models.Model):
    name = models.CharField(max_length=200, blank=True)
    weight = models.IntegerField(blank=True)
    volume = models.IntegerField(blank=True, default=0)
    where_from= models.CharField(max_length=200, blank=True)
    where_to = models.CharField(max_length=200, blank=True)
    views = models.IntegerField(verbose_name="просмотры",default= 0 , null=True,blank=True)
    field_name_sum = models.IntegerField(f'{volume} + 2 ') 
    

class HitCount(models.Model):
    visits = models.IntegerField(default=0)

