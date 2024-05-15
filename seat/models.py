from django.db import models


# Create your models here.

class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    SEAT_CLASS_CHOICES = [
        ('Economy', 'Economy'),
        ('Business', 'Business'),
        ('First Class', 'First Class'),
    ]
    seat_class = models.CharField(max_length=20, choices=SEAT_CLASS_CHOICES)
    is_reserved = models.BooleanField(default=False)  # False for available, True for reserved

    def __str__(self):
        return f" Seat number: {self.seat_number}"
