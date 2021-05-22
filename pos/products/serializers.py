from rest_framework import serializers
from products.models import ProductCategory

class ProductCategorySerilizer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory        
        fields = ['category', 'code','descriptions']