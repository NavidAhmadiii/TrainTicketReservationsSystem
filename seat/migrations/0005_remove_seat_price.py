# Generated by Django 4.2 on 2024-05-16 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0004_seat_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='price',
        ),
    ]
