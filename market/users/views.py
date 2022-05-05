from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import BaseUser, Customer, Partner
from .serializers import CustomerSerializer, BaseUserSerializer, PartnerSerializer, PartnerDetailSerializer
from goods.serializers import ProductSerializer
from goods.models import Product
from rest_framework import status, pagination, viewsets
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.

class BaseUserViewSet(viewsets.ModelViewSet):

    serializer_class = BaseUserSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_superuser:
            return BaseUser.objects.all()
        return BaseUser.objects.filter(user=self.request.user)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Customer.objects.all()
        return Customer.objects.filter(user=self.request.user)

class PartnersViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = (AllowAny, )

class PartnerViewSet(PartnersViewSet):

    serializer_class = PartnerDetailSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Partner.objects.all()
        return Partner.objects.filter(created_by__user=self.request.user)

class PartnerProducts(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Product.objects.filter(partner__created_by__user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        data = request.data
        data['partner'] = request.user.baseuser_set.first().pk
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




