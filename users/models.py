from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserModel(User):
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    telegramid = models.IntegerField()

    def __str__(self) -> str:
        return self.username
    