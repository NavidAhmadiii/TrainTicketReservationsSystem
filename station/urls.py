from django.urls import path
from .views import StationListAPIView, StationDetailAPIView

urlpatterns = [
    path('stations/', StationListAPIView.as_view(), name='station-list'),
    path('stations/<int:pk>/', StationDetailAPIView.as_view(), name='station-detail'),
]
