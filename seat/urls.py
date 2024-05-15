from django.urls import path
from .views import SeatListAPIView, SeatDetailAPIView

urlpatterns = [
    path('seats/', SeatListAPIView.as_view(), name='seat-list'),
    path('seats/<int:pk>/', SeatDetailAPIView.as_view(), name='seat-detail'),
]
