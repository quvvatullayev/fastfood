from rest_framework import generics
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import Order, OrderSerializer

class Orders(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class Order(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer