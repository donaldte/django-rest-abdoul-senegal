from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from produits.models import Category, Product
from .serializer import CategorySerializer, ProductSerializer
from rest_framework import permissions


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]