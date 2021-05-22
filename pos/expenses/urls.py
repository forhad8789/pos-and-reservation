from django.urls import path
from expenses import views


urlpatterns = [
    path('', views.ExpenseListAPIView.as_view(), name = "expenses"),
    path('<int:id>', views.ExpenseDetailsAPIView.as_view(), name = "expenses"),
    path('supplier/', views.SuppliersListAPIView.as_view(), name = "supplier"),
    path('supplier/<int:id>', views.SuppliersDetailsAPIView.as_view(), name = "supplier"),
]
