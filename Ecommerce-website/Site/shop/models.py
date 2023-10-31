from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField()
    desc = models.TextField()
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title
