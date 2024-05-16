from django.urls import path
from .views import ReservationAPIView, PaymentAPIView, ReservationDeleteAPIView

urlpatterns = [
    path('reservation/', ReservationAPIView.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', ReservationDeleteAPIView.as_view(), name='reservation-delete'),
    path('payment/', PaymentAPIView.as_view(), name='payment'),

]
