from rest_framework import serializers
from .models import StationModel


class StationSerializer(serializers.ModelSerializer):
    # capacity = serializers.IntegerField()

    class Meta:
        model = StationModel
        fields = ('id', 'name')

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=100)
    #
    # def create(self, validated_data):
    #     return StationModel.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance

    def __str__(self):
        return f"{self.name} - {self.id}"


class StationDetailSerializer(serializers.ModelSerializer):
    capacity = StationModel(serializers.IntegerField())

    class Meta:
        model = StationModel
        fields = ('id', 'name', 'capacity')


