from django.db import models


# Create your models here.
class Weather(models.Model):
    City = models.CharField(max_length=100, blank=True, default='')
    CountryCode = models.CharField(max_length=2, blank=True, default='')
