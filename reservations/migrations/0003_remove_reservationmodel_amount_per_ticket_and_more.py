# Generated by Django 4.2 on 2024-05-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_reservationmodel_amount_per_ticket_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservationmodel',
            name='amount_per_ticket',
        ),
        migrations.AlterField(
            model_name='reservationmodel',
            name='number_of_ticket',
            field=models.IntegerField(default=1),
        ),
    ]