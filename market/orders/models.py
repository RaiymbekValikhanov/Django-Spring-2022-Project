from django.db import models
from users.models import Customer, Partner
from goods.models import Product
import uuid as uuid
from .managers import OrderManager

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    objects = OrderManager()

    def __str__(self):
        return f'{self.id} order of {self.customer.user.username}'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, blank=True, null=True)

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'order item: {self.product.title}'

class Cart(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    customer = models.OneToOneField(Customer, related_name='cart', on_delete=models.CASCADE)
    cur_order = models.OneToOneField(Order, related_name='cart', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.uuid}: cart of {self.customer}'
