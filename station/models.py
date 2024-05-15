from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.


class StationModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

