from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.db import models


# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # هش کردن رمز عبور
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
