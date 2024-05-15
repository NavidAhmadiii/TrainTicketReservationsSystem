from rest_framework import serializers
from .models import ScheduleModel
from train.serializers import TrainSerializers
from station.serializers import StationSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    train = TrainSerializers()
    station = StationSerializer()
    departure_time = serializers.DateTimeField(read_only=True)
    arrived_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ScheduleModel
        fields = ('id', 'train', 'station', 'departure_time', 'arrived_time')
