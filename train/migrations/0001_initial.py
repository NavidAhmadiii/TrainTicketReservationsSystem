# Generated by Django 4.2 on 2024-05-13 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_number', models.IntegerField(unique=True)),
                ('destination_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin-destination+', to='station.stationmodel')),
                ('origin_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin-station+', to='station.stationmodel')),
            ],
        ),
    ]
