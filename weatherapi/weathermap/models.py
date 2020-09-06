from django.db import models
from django.db.models.query import QuerySet
from CustomQuerySet.models import CustomQuerySetManager


# Create your models here.
class Weather(models.Model):
    City = models.CharField(max_length=100, blank=True, default='')
    CountryCode = models.CharField(max_length=2, blank=True, default='')

    class QuerySet(QuerySet):
        def active_for_account(self, account, *args, **kwargs):
            return self.filter(account=account, deleted=False, *args, **kwargs)


