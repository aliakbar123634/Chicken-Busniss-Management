from django.db import models
class Product(models.Model):
    UNIT_CHOICES = (
        ('kg', 'KG'),
        ('piece', 'Piece'),
        ('box', 'Box'),
    )

    name = models.CharField(max_length=255)
    # sku = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2)
    sale_price = models.DecimalField(max_digits=12, decimal_places=2)
    current_stock = models.IntegerField(default=0)
    minimum_stock_alert = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


#        python manage.py makemigrations products
#        python manage.py migrate products    