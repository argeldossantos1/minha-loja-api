from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from rest_framework import viewsets
from .serializer import ProductSerializer


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-category')
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'brand', 'category']