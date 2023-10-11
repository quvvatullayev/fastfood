from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import Category, CategorySerializer

class CategorysView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer