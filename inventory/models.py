from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class InventoryMovement(models.Model):
    MOVEMENT_TYPE = (
    ('purchase', 'Purchase'),
    ('sale', 'Sale'),
    ('adjustment', 'Adjustment'),
    ('return', 'Return'),
)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movement_type = models.CharField(
        max_length=20,
        choices=MOVEMENT_TYPE
    )
    reference_type = models.CharField(max_length=50)
    reference_id = models.IntegerField()
    quantity = models.IntegerField()
    stock_before = models.IntegerField()
    stock_after = models.IntegerField()
    notes = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.movement_type} of {self.quantity}{self.product.name}"