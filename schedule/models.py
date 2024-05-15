from django.db import models
from django.utils import timezone
from train.models import TrainModel
from station.models import StationModel


# Create your models here.


class ScheduleModel(models.Model):
    train = models.ForeignKey(TrainModel, on_delete=models.CASCADE)
    station = models.ForeignKey(StationModel, on_delete=models.CASCADE)
    departure_time = models.DateTimeField(auto_now_add=True)
    arrived_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.train} - {self.departure_time}"

    def save(self, *args, **kwargs):
        if self.arrived_time is not None:
            self.arrived_time = timezone.now()
        super().save(*args, **kwargs)
