from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import Product, ProductSerializer

class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    