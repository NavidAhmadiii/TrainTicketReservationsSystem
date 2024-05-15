from rest_framework import serializers
from station.models import StationModel
from station.serializers import StationSerializer
from .models import TrainModel


class TrainSerializers(serializers.ModelSerializer):
    # when show data to user by name
    # origin_station = StationSerializer()
    # destination_station = StationSerializer()

    # when post data to database by id
    origin_station = serializers.PrimaryKeyRelatedField(queryset=StationModel.objects.all())
    destination_station = serializers.PrimaryKeyRelatedField(queryset=StationModel.objects.all())

    class Meta:
        model = TrainModel
        fields = ('id', 'train_number', 'origin_station', 'destination_station')

    # def create(self, validated_data):
    #     origin_station_id = validated_data.pop('origin_station_id')
    #     destination_station_id = validated_data.pop('destination_station_id')
    #     validated_data['origin_station'] = StationModel.objects.get(id=origin_station_id)
    #     validated_data['destination_station'] = StationModel.objects.get(id=destination_station_id)
    #     return TrainModel.objects.create(**validated_data)
