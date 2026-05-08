from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/' , views.CustomerCreateView , name='create_customer'),
]