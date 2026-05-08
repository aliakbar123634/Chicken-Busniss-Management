from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/' , views.ProductCreateView , name='product_create'),
    path('list/' , views.ProductListView , name='product_list'),
    path('detail/<int:pk>/' , views.ProductDetailView , name='product_detail'),
    path('update/<int:pk>/' , views.ProductUpdateView , name='product_update'),
    path('delete/<int:pk>/' , views.ProductDeleteView , name='product_delete'),
    path('low-stock/' , views.low_stock_products , name='low_stock_products'),
]


#         python manage.py runserver