from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import UserModel, UserSerializer

class Users(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class User(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer