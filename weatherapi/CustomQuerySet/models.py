from django.db import models
from django.db.models.query import QuerySet


class CustomQuerySetManager(models.Manager):
    """A re-usable Manager to access a custom QuerySet"""

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            # don't delegate internal methods to the queryset
            if attr.startswith('__') and attr.endswith('__'):
                raise
            return getattr(self.get_query_set(), attr, *args)

    def get_query_set(self):
        return self.model.QuerySet(self.model, using=self._db)

    def get_query_set(self):
        return self.model.QuerySet(self.model, using=self._db)
