from django.db import models
from station.models import StationModel


# Create your models here.


class TrainModel(models.Model):
    train_number = models.IntegerField(unique=True)
    origin_station = models.ForeignKey(StationModel, on_delete=models.CASCADE, related_name='origin-station+')
    destination_station = models.ForeignKey(StationModel, on_delete=models.CASCADE, related_name='origin-destination+')

    def __str__(self):
        return f"{self.origin_station} to {self.destination_station}"
