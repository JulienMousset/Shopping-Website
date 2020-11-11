from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    ##quantity = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class Cart(models.Model):
    items = models.ManyToManyField(Product)
    ## products = ArrayField(models.CharField(max_length=255), default=[])
    ## quantities = ArrayField(models.PositiveIntegerField(), default=[])
    ## Add a cart on/off variable?