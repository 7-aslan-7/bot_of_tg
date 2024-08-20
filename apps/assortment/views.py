from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class NewArrivalsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


