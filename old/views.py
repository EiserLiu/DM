from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UserSerializer


class UserView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
