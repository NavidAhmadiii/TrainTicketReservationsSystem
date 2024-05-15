from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ReservationModel
from .serializers import ReservationInputSerializer, ReservationOutputSerializer


# Create your views here.

class ReservationAPIView(APIView):

    def get(self, request):
        reservations = ReservationModel.objects.all()
        serializer = ReservationOutputSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # برای دریافت اطلاعات جدید از دیتابیس
            new_reservation = ReservationModel.objects.latest('id')
            output_serializer = ReservationOutputSerializer(new_reservation)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
