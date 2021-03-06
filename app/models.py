from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    items = models.ManyToManyField(Product)
