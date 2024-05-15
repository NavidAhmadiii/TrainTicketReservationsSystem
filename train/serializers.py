from rest_framework import serializers
from station.models import StationModel
from station.serializers import StationSerializer
from .models import TrainModel


# class TrainSerializers(serializers.ModelSerializer):
#     # when show data to user by name
#     # origin_station = StationSerializer()
#     # destination_station = StationSerializer()
#
#     # when post data to database by id
#     origin_station = serializers.PrimaryKeyRelatedField(queryset=StationModel.objects.all())
#     destination_station = serializers.PrimaryKeyRelatedField(queryset=StationModel.objects.all())
#
#     class Meta:
#         model = TrainModel
#         fields = ('id', 'train_number', 'origin_station', 'destination_station')
#

class TrainInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainModel
        fields = ('train_number', 'origin_station', 'destination_station')


class TrainOutputSerializer(serializers.ModelSerializer):
    origin_station = StationSerializer()
    destination_station = StationSerializer()

    class Meta:
        model = TrainModel
        fields = '__all__'
