from rest_framework import serializers
from .models import UserModel, Cart, Order

class UserSerializer(serializers.ModelSerializer):
    class Model:
        model = UserModel
        fields = ['id', 'username', 'phonenumber', 'address', 'telegramid']

