from django.db import models
from django.contrib.auth.models import User

class Logistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, blank=True)
    color_type = (
        (1, 'grey'),
        (2, 'silver'),
        (3, 'black'),
        (4, 'red'),
        (5, 'blue'),
    )
    color = models.CharField(max_length=200, choices=color_type, blank=True)
    vin = models.IntegerField(blank=True, default=0)
    brand_type = (
        (1, 'apple'),
        (2, 'asus'),
        (3, 'dell'),
        (4, 'acer'),
        (5, 'lenovo'),
    )
    brand = models.CharField(max_length=200, choices=brand_type, blank=True)
    cpu = models.CharField(max_length=200, blank=True)
    ram = models.IntegerField(blank=True, default=0)
    memory = models.IntegerField(blank=True, default=0)
    display_type = (
        (1, '4096 x 2160'),
        (2, '2048 x 1080'),
        (3, '1920 x 1080'),
        (4, '1024 x 768'),
    )
    display = models.CharField(max_length=200, choices=display_type, blank=True)
    battery = models.IntegerField(blank=True, default=0)
    prod = models.CharField(max_length=200, blank=True)
