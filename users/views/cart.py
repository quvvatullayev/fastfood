from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import Cart, CartSerializer

class Carts(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class Cart(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
