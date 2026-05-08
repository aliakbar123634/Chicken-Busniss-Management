from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('accountant', 'Accountant'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username




#      python manage.py runserver
#      python manage.py makemigrations
#      python manage.py migrate



#      python manage.py createsuperuser














#           python manage.py makemigrations
#           python manage.py migrate