from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.authentication.views.register_user_view import RegisterUserView

urlpatterns = [
    path('api/register', RegisterUserView.as_view()),
    path('api/login', TokenObtainPairView.as_view()),
    path('api/refresh_token', TokenRefreshView.as_view()),
]
