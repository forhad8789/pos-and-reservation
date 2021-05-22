from django.db import models
from authentication.models import User
# Create your models here.

class Expense(models.Model):

    CATEGORY_OPTIONS = [
        ('ONLINE_SERVICE','ONLINE_SERVICE'),
        ('TRAVEL','TRAVEL'),
        ('FOOD','FOOD'),
        ('RENT','RENT'),
        ('OTHERS','OTHERS')
    ]

    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)

    class Meta:
        db_table = 'expense'


class Suppliers(models.Model):
    name = models.CharField(max_length=100)
    phone = models.TextField(null=True)
    email = models.TextField(null=True)
    description = models.TextField()
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'suppliers'



