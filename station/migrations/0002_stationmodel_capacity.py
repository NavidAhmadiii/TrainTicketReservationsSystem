# Generated by Django 4.2 on 2024-05-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stationmodel',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
    ]