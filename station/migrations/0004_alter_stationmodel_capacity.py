# Generated by Django 4.2 on 2024-05-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0003_alter_stationmodel_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationmodel',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
    ]