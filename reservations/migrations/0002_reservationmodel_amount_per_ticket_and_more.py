# Generated by Django 4.2 on 2024-05-16 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationmodel',
            name='amount_per_ticket',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservationmodel',
            name='number_of_ticket',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
