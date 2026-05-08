from django.db import models

from purchases.models import Purchase
from sales.models import Sale
from customers.models import Customer
from suppliers.models import Supplier
from django.contrib.auth.models import User
# Create your models here.
class Payment(models.Model):
    PAYMENT_DIRECTION = (
    ('incoming', 'Incoming'),
    ('outgoing', 'Outgoing'),
)

    PAYMENT_METHOD = (
    ('cash', 'Cash'),
    ('bank', 'Bank'),
    ('jazzcash', 'JazzCash'),
    ('easypaisa', 'EasyPaisa'),
)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, blank=True, null=True)

    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, blank=True, null=True)

    payment_direction = models.CharField(
        max_length=20,
    choices=PAYMENT_DIRECTION
)

    amount = models.DecimalField(max_digits=12, decimal_places=2)

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD
    )

    reference_number = models.CharField(
    max_length=255,
    blank=True,
    null=True
)

    notes = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)