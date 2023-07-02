from django.db.models import Q
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from user.models import User, Location, Ad
from user.serializers import UserListSerializer, LocationSerializer, AdListSerializer, UserDetailSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        category_id = request.GET.getlist('cat', None)
        category = None
        for i in category_id:
            if category is None:
                category = Q(category=i)
            else:
                category |= Q(category=i)
        if category:
            self.queryset = self.queryset.filter(category)

        name = request.GET.get('text', None)
        if name:
            self.queryset = self.queryset.filter(name__icontains=name)

        location = request.GET.get('loc', None)
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location).order_by('id')

        range_from = request.GET.get('ran_from', None)
        range_to = request.GET.get('ran_to', None)
        if range_from and range_to:
            self.queryset = self.queryset.filter(price__range=(range_from, range_to))

        return super().get(request, *args, **kwargs)

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    # permission_classes = [IsAuthenticated]