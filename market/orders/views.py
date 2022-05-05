from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Order, OrderItem, Cart
from .serializers import OrderSerializer, OrderItemSerializer, CartSerializer
from rest_framework import status, pagination, viewsets
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.

class CartView(ListCreateAPIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(customer__user=self.request.user)


class UserOrdersView(ListCreateAPIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(customer__user=self.request.user)

class UserOrderItemsView(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer






