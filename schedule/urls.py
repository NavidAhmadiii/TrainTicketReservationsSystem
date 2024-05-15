from django.urls import path
from .views import ScheduleAPIView

urlpatterns = [
    # path('schedules/', ScheduleAPIView.as_view(), name='schedule-list'),
    path('schedules/<int:pk>/', ScheduleAPIView.as_view(), name='schedule-detail'),
]
