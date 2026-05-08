from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notification(models.Model):
    NOTIFICATION_TYPE = (
    ('low_stock', 'Low Stock'),
    ('payment_due', 'Payment Due'),
    ('overdue', 'Overdue'),
    ('system', 'System'),
)

    title = models.CharField(max_length=255)

    message = models.TextField()

    notification_type = models.CharField(
        max_length=30,
    choices=NOTIFICATION_TYPE
)

    related_model = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    related_object_id = models.IntegerField(
    blank=True,
    null=True
)

    is_read = models.BooleanField(default=False)

    sent_to = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.get_notification_type_display()}"