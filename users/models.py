from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class UserModel(User):
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    telegramid = models.IntegerField()

    def __str__(self) -> str:
        return self.username
    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ['-id']
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loocation = models.CharField(max_length=225)
    time = models.DateTimeField()

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ['-id']
    
    