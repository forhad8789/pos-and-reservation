from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from products.serializers import ProductCategorySerilizer
from products.models import ProductCategory
from rest_framework import permissions


class ProductCategoryListApiView(ListCreateAPIView):
    serilizer_class = ProductCategorySerilizer
    # query_set = ProductCategory.objects.all()

    def perform_create(self, serializer):
        return serializer.save(self.request)
    
    def get_queryset(self):
        print("hi")
        return self.request.user