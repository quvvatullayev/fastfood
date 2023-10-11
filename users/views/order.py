from rest_framework import generics
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import Order, OrderSerializer, UserModel, UserSerializer

class OrdersView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request:Request, *args, **kwargs):
        telegramid = kwargs['telegramid']
        user_obj = UserModel.objects.get(telegramid = telegramid)

        orders_obj = Order.objects.filter(user = user_obj)
        orders = OrderSerializer(orders_obj, many = True)

        return Response({
            'orders':orders.data
        })

class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer