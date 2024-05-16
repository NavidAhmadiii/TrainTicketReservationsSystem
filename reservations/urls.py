from django.urls import path
from .views import ReservationAPIView, PaymentAPIView

urlpatterns = [
    path('reservation/', ReservationAPIView.as_view(), name='reservation-list'),
    path('payment/', PaymentAPIView.as_view(), name='payment'),

]
