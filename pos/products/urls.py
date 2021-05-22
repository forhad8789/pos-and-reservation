from django.urls import path
from products.views import ProductCategoryListApiView
urlpatterns = [
    path('', ProductCategoryListApiView.as_view(), name = "product"),
    path('<int:id>', ProductCategoryListApiView.as_view(), name = "product"),
]
