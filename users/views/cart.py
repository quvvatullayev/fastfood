from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import Cart, CartSerializer, UserModel, UserSerializer

class CartsView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def list(self, request:Request, *args, **kwargs):
        telegramid = kwargs['telegramid']
        user_obj = UserModel.objects.get(telegramid = telegramid)

        carts_obj = Cart.objects.filter(user = user_obj)
        carts = CartSerializer(carts_obj, many = True)

        return Response({'carts':carts.data})

class CartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
