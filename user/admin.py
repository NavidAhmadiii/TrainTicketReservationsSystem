from django.contrib import admin
from .models import CustomUser


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')


admin.site.register(CustomUser, UserAdmin)
