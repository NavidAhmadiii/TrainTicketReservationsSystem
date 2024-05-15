from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TrainSerializers
from .models import TrainModel


# Create your views here.

class TrainListAPIView(APIView):

    def get(self, request):
        trains = TrainModel.objects.all()
        serializer = TrainSerializers(trains, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.error_messages)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class TrainDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return TrainModel.objects.get(pk=pk)
        except TrainModel.DoesNotExite:
            raise Http404

    def get(self, request, pk):
        train = self.get_object(pk)
        serializer = TrainSerializers(train)
        return Response(serializer.data)

    def put(self, request, pk):
        train = self.get_object(pk)
        serializer = TrainSerializers(train, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        train = self.get_object(pk)
        train.delete()
        return Response({'message': 'delete successful'}, status=status.HTTP_204_NO_CONTENT)
