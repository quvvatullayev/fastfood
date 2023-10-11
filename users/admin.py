from django.contrib import admin
from .models import UserModel, Cart, Order
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register([UserModel, Cart, Order])
admin.site.unregister([Group])
