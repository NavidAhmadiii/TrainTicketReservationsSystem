from django.urls import path
from .views import LoginAPIView, LogoutAPIView, ChangePasswordAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    # path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
