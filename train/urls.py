from django.urls import path
from .views import TrainListAPIView, TrainDetailAPIView

urlpatterns = [
    path('trains/', TrainListAPIView.as_view(), name='train-list'),
    path('trains/<int:pk>/', TrainDetailAPIView.as_view(), name='train-ditail'),
]
