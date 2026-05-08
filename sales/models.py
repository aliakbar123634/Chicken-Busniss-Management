from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from products.models import Product

# Create your models here.

class Sale(models.Model):
    PAYMENT_STATUS = (
    ('paid', 'Paid'),
    ('partial', 'Partial'),
    ('unpaid', 'Unpaid'),
)

    SALE_TYPE = (
    ('cash', 'Cash'),
    ('credit', 'Credit'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    invoice_number = models.CharField(max_length=100, unique=True)

    date = models.DateField()

    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    remaining_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS)

    sale_type = models.CharField(max_length=20, choices=SALE_TYPE)

    notes = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sale{self.invoice_number} to {self.customer.name}"



class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    rate = models.DecimalField(max_digits=12, decimal_places=2)

    total = models.DecimalField(max_digits=12, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
