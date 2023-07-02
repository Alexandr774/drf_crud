from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from autentication import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]
