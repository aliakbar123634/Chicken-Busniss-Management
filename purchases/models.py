from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from suppliers.models import Supplier

# Create your models here.
class Purchase(models.Model):
    PAYMENT_STATUS = (
    ('paid', 'Paid'),
    ('partial', 'Partial'),
    ('unpaid', 'Unpaid'),
)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    invoice_number = models.CharField(max_length=100, unique=True)

    date = models.DateField()

    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    remaining_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS)

    notes = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Purchase {self.invoice_number} from {self.supplier.name}"

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"