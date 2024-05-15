from django.contrib import admin
from .models import Seat


# Register your models here.

class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'seat_class', 'seat_number', 'is_reserved')


admin.site.register(Seat, SeatAdmin)
