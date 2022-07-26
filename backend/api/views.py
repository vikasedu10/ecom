from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from frontend.models import Product

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()