from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user.username}'

class Customer(BaseUser):
    billing_info = models.CharField(max_length=255, blank=True, null=True)

class Partner(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(BaseUser, related_name='partner', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


