from django.db import models

# Create your models here.

class Product(models.Model):
    ## image = models.TextField()
    image = models.ImageField(blank=True, null=True)
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    items = models.ManyToManyField(Product)
    ## products = ArrayField(models.CharField(max_length=255), default=[])
    ## quantities = ArrayField(models.PositiveIntegerField(), default=[])
    ## Add a cart on/off variable?