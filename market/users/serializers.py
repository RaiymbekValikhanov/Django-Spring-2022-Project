import re

from .models import Partner, Customer
from rest_framework import serializers
from goods.serializers import ProductSerializer

class BaseUserSerializer(serializers.Serializer):
    email = serializers.EmailField(source='user')
    username = serializers.CharField(source='user')

class CustomerSerializer(BaseUserSerializer):
    billing_info = serializers.CharField(max_length=255)

    def validate_billing_info(self, value):
        reg = re.compile(r'^\d{4}$')
        if reg.match(value):
            return value
        raise ValueError

class PartnerSerializer(serializers.ModelSerializer):
    created_by = BaseUserSerializer()

    class Meta:
        model = Partner
        fields = ('name', 'created_at', 'created_by', )

class PartnerDetailSerializer(PartnerSerializer):
    products = ProductSerializer(many=True)

    class Meta(PartnerSerializer.Meta):
        fields = PartnerSerializer.Meta.fields + ('products', )
