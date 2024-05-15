from rest_framework import serializers

from station.models import StationModel
from train.models import TrainModel
from .models import ScheduleModel
from train.serializers import TrainSerializers
from station.serializers import StationSerializer


# class ScheduleSerializer(serializers.ModelSerializer):
#     # add an information for train and station in response
#     # train = TrainSerializers()
#     # station = StationSerializer()
#     departure_time = serializers.DateTimeField(read_only=True)
#     arrived_time = serializers.DateTimeField(read_only=True)
#
#     class Meta:
#         model = ScheduleModel
#         fields = ('id', 'train', 'station', 'departure_time', 'arrived_time')


class FullTrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainModel
        fields = ('id', 'train_number', 'origin_station', 'destination_station')


class FullStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationModel
        fields = ('id', 'name', 'capacity')


class ScheduleInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleModel
        fields = ('train', 'station', 'departure_time', 'arrived_time')


class ScheduleOutputSerializer(serializers.ModelSerializer):
    train = FullTrainSerializer()
    station = FullStationSerializer()

    class Meta:
        model = ScheduleModel
        fields = ('id', 'train', 'station', 'departure_time', 'arrived_time')
