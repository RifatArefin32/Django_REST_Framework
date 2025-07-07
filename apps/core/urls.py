from django.urls import path
from apps.core import views

urlpatterns = [
    # path('products/', views.product_list),
    path('products/', views.ProductListApiView.as_view()),
    path('products_info/', views.products_info),
    # path('products/<int:pk>/', views.product_details),
    # path('products/<int:pk>/', views.ProductDetailApiView.as_view()),
    path('products/<int:id>/', views.ProductDetailApiView.as_view()),
    # path('orders/', views.order_list),
    path('orders/', views.OrderListApiView.as_view()),
]
