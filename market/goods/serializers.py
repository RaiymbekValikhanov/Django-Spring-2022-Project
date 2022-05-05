from abc import ABC

from .models import Product, Category, Review
from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.CharField(required=False)


class ReviewSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    rating = serializers.IntegerField(min_value=0, max_value=5)

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'quantity', 'category', 'partner')

    def validate_category(self, value):
        try:
            category = Category.objects.get(**value)
            return category
        except Exception as e:
            raise e

    def validate_price(self, value):
        if value < 0 or value > 100000:
            raise ValueError
        return value

    def validate_quantity(self, value):
        if value < 0 or value > 100:
            raise ValueError
        return value

class ProductReviewSerializer(ProductSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ('description', 'reviews', )

class CategoryProductsSerializer(CategorySerializer):
    products = ProductSerializer(many=True)



