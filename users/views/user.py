from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import UserModel, UserSerializer

class UsersView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer