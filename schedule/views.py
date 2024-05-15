from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ScheduleModel
from .serializers import ScheduleInputSerializer, ScheduleOutputSerializer


# Create your views here.

# class ScheduleAPIView(APIView):
#
#     def get(self, request):
#         schedules = ScheduleModel.objects.all()
#         serializer = ScheduleSerializer(schedules, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ScheduleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'New schedule added'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleAPIView(APIView):

    def get(self, request, pk):
        try:
            schedule = ScheduleModel.objects.get(pk=pk)
            serializer = ScheduleOutputSerializer(schedule)
            return Response(serializer.data)
        except ScheduleModel.DoesNotExist:
            return Response({'message': 'Schedule not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        input_serializer = ScheduleInputSerializer(data=request.data)
        if input_serializer.is_valid():
            input_serializer.save()
            instance = input_serializer.instance
            output_serializer = ScheduleOutputSerializer(instance)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
