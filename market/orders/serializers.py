from rest_framework import serializers
from .models import Order, OrderItem, Cart
from goods.models import Product

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'created_at', 'address')

class OrderDetailSerializer(OrderSerializer):
    class Meta(OrderSerializer.Meta):
        fields = OrderSerializer.Meta.fields + ('done', )
        depth = 2

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'order')

    def validate_product(self, value):
        product = Product.objects.get(**value)
        return product


class CartSerializer(serializers.ModelSerializer):
    cur_order = OrderDetailSerializer()

    class Meta:
        model = Cart
        fields = ('uuid', 'cur_order')

