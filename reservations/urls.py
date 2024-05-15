from django.urls import path
from .views import ReservationAPIView

urlpatterns = [
    path('reservation/', ReservationAPIView.as_view(), name='reservation-list'),
]
