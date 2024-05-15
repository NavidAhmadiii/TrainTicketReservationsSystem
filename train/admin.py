from django.contrib import admin
from .models import TrainModel


# Register your models here.

@admin.register(TrainModel)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('id', 'train_number', 'origin_station', 'destination_station')
