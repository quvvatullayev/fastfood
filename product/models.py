from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to='../categoryimgs')
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["-id"]
        

class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    img = models.ImageField(upload_to='../productimgs')
    price = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-id']
        

