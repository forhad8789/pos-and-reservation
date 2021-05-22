from django.db import models
from expenses.models import Suppliers

# Create your models here.
class ProductCategory(models.Model):
    
    category = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)
    descriptions = models.TextField()
    
class Products(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    sku = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    srp_price = models.DecimalField(max_digits=50, decimal_places=2)
    image = models.TextField(null=True)
    supplier_id = models.ForeignKey(to=Suppliers, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

    