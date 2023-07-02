from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from autentication.models import User
from autentication.seraializer import UserCreateSerializer


class CreateUserView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer