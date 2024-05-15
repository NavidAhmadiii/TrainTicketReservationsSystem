from django.db import models
from user.models import CustomUser
from seat.models import Seat
from schedule.models import ScheduleModel


# Create your models here.


class ReservationModel(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    schedule = models.ForeignKey(ScheduleModel, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default='pending')
