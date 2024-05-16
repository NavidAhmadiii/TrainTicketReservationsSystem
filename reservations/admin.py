from django.contrib import admin
from .models import ReservationModel


# Register your models here.
@admin.register(ReservationModel)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'status',)
