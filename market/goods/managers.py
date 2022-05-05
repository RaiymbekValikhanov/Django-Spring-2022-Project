from django.db import models

class ProductManager(models.Manager):
    def products_of_partner(self, partner):
        return self.filter(partner__id=partner.id)

    def product_of_category(self, category):
        return self.filter(category__id=category.id)


class CategoryManager(models.Manager):
    def all_products(self):
        return self.products

class ReviewManager(models.Manager):
    def avg_rating(self):
        return self.aggregate(models.Avg('rating'))