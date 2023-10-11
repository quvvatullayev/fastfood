from rest_framework import generics
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import Order, OrderSerializer

class OrdersView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer