from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializer import ExpenseSerializer, SupplierSerializer
from .models import Roles
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class RoleListAPIView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Roles.objects.all()
    


    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner_id = 1)