from __future__ import unicode_literals

from django.db import models

# Create your models here.

class URLs(models.Model):
    larga = models.CharField(max_length=32)
    corta = models.IntegerField()
