from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializer import ExpenseSerializer, SupplierSerializer
from .models import Expense, Suppliers
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permissions_classes = (IsAuthenticated,IsOwner,)


    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner_id = 1)

class ExpenseDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permissions_classes = (IsAuthenticated,IsOwner,)
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class SuppliersListAPIView(ListCreateAPIView):
    serializer_class = SupplierSerializer
    queryset = Suppliers.objects.all()
    permissions_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.all()

class SuppliersDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Suppliers.objects.all()
    permissions_classes = (IsAuthenticated,)
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return Suppliers.objects.all()

     