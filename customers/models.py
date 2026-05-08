from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    address = models.TextField(blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    balance_limit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)