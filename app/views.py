from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from . models import Product, Cart
from . serializers import ProductSerializer, CartSerializer

class ProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class CartView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)
