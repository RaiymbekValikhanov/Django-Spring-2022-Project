from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Category, Product, Review
from .serializers import CategorySerializer, CategoryProductsSerializer, ProductSerializer, ReviewSerializer, ProductReviewSerializer
from rest_framework import status, pagination
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
@api_view(['GET'])
def get_all_products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_categories(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)

class ProductView(APIView):

    def check_permissions(self, request):
        if request.method != 'GET':
            return request.user.is_superuser
        return True

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Http404

    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductReviewSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = self.get_object(id)
        if request.user != product.partner.created_by.user:
            return Response(status.HTTP_401_UNAUTHORIZED)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = self.get_object(id)
        if request.user != product.partner.created_by.user:
            return Response(status.HTTP_401_UNAUTHORIZED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryView(APIView):

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Product.DoesNotExist:
            return Http404

    def get(self, request, id):
        category = self.get_object(id)
        serializer = CategoryProductsSerializer(category)
        return Response(serializer.data)



