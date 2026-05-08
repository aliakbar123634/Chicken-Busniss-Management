from django.db import models

from sales.models import Sale

# Create your models here.
class Receipt(models.Model):
    sale = models.OneToOneField(Sale, on_delete=models.CASCADE)

    receipt_number = models.CharField(
        max_length=100,
        unique=True
    )

    pdf_file = models.FileField(
        upload_to='receipts/'
    )

    printed_count = models.IntegerField(default=0)

    last_printed_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Receipt {self.receipt_number} for Sale {self.sale.id}"