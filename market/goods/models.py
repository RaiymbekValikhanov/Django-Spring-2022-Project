from django.db import models
from users.models import Customer, Partner
from .managers import ProductManager, CategoryManager, ReviewManager

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=500, unique=True, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    objects = CategoryManager()

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=500, unique=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    partner = models.ForeignKey(Partner, related_name='products', on_delete=models.PROTECT, null=True, blank=True)
    objects = ProductManager()

    def __str__(self):
        return f'{self.title}'

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField()
    objects = ReviewManager()

    def __str__(self):
        return f'Review of {self.product} from {self.customer}'

