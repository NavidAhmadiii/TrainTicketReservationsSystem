from django.contrib import admin
from .models import StationModel


# Register your models here.
@admin.register(StationModel)
class StationAdminModel(admin.ModelAdmin):
    list_display = ['id', 'name']
