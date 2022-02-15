from django.db import models

# Create your models here.
class ProductItem(models.Model):
    # product_id = models.PositiveIntegerField()
    product_name = models.CharField(max_length=200)
    product_price = models.CharField(max_length=200)
    product_quantity = models.CharField(max_length=200)