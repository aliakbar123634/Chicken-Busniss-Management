from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/' , views.CreateSupplierView , name='supplier_create'),
    path('list/' , views.ListSupplierView , name='supplier_list'),
    path('detail/<int:pk>/' , views.DetailSupplierView , name='supplier_detail'),
    path('update/<int:pk>/' , views.UpdateSupplierView , name='supplier_update'),
    path('delete/<int:pk>/' , views.SupplierDeleteView , name='supplier_delete'),
]


#         python manage.py runserver