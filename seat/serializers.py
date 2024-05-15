from rest_framework import serializers
from .models import Seat


class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = ('id', 'seat_number', 'seat_class')


class SeatDetailSerializer(serializers.ModelSerializer):
    is_reserved = serializers.BooleanField()

    class Meta:
        model = Seat
        fields = ('id', 'seat_number', 'seat_class', 'is_reserved')
