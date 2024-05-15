from rest_framework import serializers
from .models import ScheduleModel


class ScheduleSerializer(serializers.ModelSerializer):
    departure_time = serializers.DateTimeField(read_only=True)
    arrived_time = serializers.DateTimeField(read_only=True)

    class Meta:
        models = ScheduleModel
        fields = ('id', 'train', 'station', 'departure_time', 'arrived_time')
