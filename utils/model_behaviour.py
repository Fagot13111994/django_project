from django.db import models


class Timestampable(models.Model):
    data_created = models.DateTimeField(auto_now_add=True)
    data_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
