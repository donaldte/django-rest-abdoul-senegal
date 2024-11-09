from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .permissions import AuthorPermission
from produits.models import Category, Product
from .serializer import CategorySerializer, ProductSerializer
from rest_framework import permissions
from rest_framework.decorators import permission_classes



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AuthorPermission] #permissions.AllowAny, permissions.IsAdminUser, permissions.IsAuthenticated permissions.IsAuthenticatedOrReadOnly
    
    # # @permission_classes([])
    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     email = data.get('email')
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
        
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]