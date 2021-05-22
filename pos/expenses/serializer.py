from rest_framework import serializers
from .models import Expense, Suppliers

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ['id','date', 'description', 'amount','category']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        #fields = ['name', 'description']
        fields = '__all__'