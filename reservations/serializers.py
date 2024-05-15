from rest_framework import serializers

from seat.serializers import SeatSerializer
from schedule.serializers import ScheduleOutputSerializer
from user.serializers import CustomUserSerializer
from .models import ReservationModel


class ReservationInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationModel
        fields = ('user', 'schedule', 'seat')


class ReservationOutputSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    schedule = ScheduleOutputSerializer()
    seat = SeatSerializer()

    class Meta:
        model = ReservationModel
        fields = '__all__'
