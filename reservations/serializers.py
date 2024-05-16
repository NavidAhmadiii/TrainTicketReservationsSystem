from rest_framework import serializers

from seat.serializers import SeatSerializer
from schedule.serializers import ScheduleOutputSerializer
from user.serializers import CustomUserSerializer
from .models import ReservationModel


class ReservationInputSerializer(serializers.ModelSerializer):
    number_of_tickets = serializers.IntegerField()  # اضافه کردن فیلد تعداد بلیط‌ها

    class Meta:
        model = ReservationModel
        fields = ('user', 'schedule', 'seat', 'number_of_tickets')

    def create(self, validated_data):
        number_of_tickets = validated_data.pop('number_of_tickets')
        reservation = ReservationModel.objects.create(**validated_data)
        ticket_price = 1000
        total_amount = ticket_price * number_of_tickets
        reservation.total_amount = total_amount
        reservation.save()

        return reservation


class ReservationOutputSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    schedule = ScheduleOutputSerializer()
    seat = SeatSerializer()

    class Meta:
        model = ReservationModel
        fields = '__all__'
