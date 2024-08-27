from rest_framework import viewsets, generics
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class NewArrivalsList(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-created_at')[:10]  
    serializer_class = ProductSerializer
