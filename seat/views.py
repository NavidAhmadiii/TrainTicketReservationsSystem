from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Seat
from .serializers import SeatSerializer, SeatDetailSerializer


# Create your views here.

class SeatListAPIView(APIView):
    def get(self, request):
        seats = Seat.objects.all()
        serializer = SeatSerializer(seats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SeatDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Seat.objects.get(pk=pk)
        except Seat.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        seat = self.get_object(pk)
        serializer = SeatDetailSerializer(seat)
        return Response(serializer.data)

    def put(self, request, pk):
        seat = self.get_object(pk)
        serializer = SeatDetailSerializer(seat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        seat = self.get_object(pk)
        seat.delete()
        return Response({'message': 'seat has been deleted'}, status=status.HTTP_204_NO_CONTENT)
