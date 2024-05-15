from django.contrib import admin
from .models import ScheduleModel


# Register your models here.

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'train')


admin.site.register(ScheduleModel, ScheduleAdmin)
