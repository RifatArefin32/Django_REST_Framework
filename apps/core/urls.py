from django.urls import path
from apps.core import views

urlpatterns = [
    path('products/', views.product_list),
    path('products_info/', views.products_info),
    path('products/<int:pk>/', views.product_details),
    path('orders/', views.order_list),
]
