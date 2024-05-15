from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StationModel
from .serializers import StationSerializer, StationDetailSerializer


# Create your views here.

class StationListAPIView(APIView):

    def get(self, request):
        stations = StationModel.objects.all()
        serializer = StationSerializer(stations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StationDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StationDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return StationModel.objects.get(pk=pk)
        except StationModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        station = self.get_object(pk)
        serializer = StationDetailSerializer(station)
        return Response(serializer.data)

    def put(self, request, pk):
        station = self.get_object(pk)
        serializer = StationDetailSerializer(station, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        station = self.get_object(pk)
        station.delete()
        return Response({'message': 'station was deleted'}, status=status.HTTP_204_NO_CONTENT)
