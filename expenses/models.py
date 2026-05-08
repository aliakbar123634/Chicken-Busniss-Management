from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = (
    ('transport', 'Transport'),
    ('salary', 'Salary'),
    ('electricity', 'Electricity'),
    ('maintenance', 'Maintenance'),
    ('other', 'Other'),
)

    title = models.CharField(max_length=255)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    amount = models.DecimalField(max_digits=12, decimal_places=2)

    date = models.DateField()

    notes = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} - {self.amount}"
    

#       python manage.py runserver    