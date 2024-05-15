# Generated by Django 4.2 on 2024-05-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0003_rename_status_seat_is_reserved'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]