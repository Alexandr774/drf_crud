from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'location', views.LocationViewSet)

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('create/', views.UserCreateView.as_view()),
    path('ad/', views.AdListView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view())
]

urlpatterns += router.urls
