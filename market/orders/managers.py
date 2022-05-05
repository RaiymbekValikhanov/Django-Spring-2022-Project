from django.db import models

class OrderManager(models.Manager):
    def orders_of_user(self, user):
        return self.filter(customer=user)

    def active_orders_of_user(self, user):
        return self.orders_of_user(user).filter(done=False)

    def total_items_quantity(self):
        return self.first().items.aggreate(models.Sum('quantity'))

class CartManager(models.Manager):
    def items_quantity(self):
        return self.first().cur_order.total_items_quantity()

