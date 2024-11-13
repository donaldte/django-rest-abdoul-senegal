from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .permissions import AuthorPermission
from produits.models import Category, Product
from .serializer import CategorySerializer, ProductSerializer
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class CategoryThrottle(UserRateThrottle, AnonRateThrottle):
    scope = 'category'
    rate = '2/min'
    rate_key = 'ip'
    

@permission_classes([AuthorPermission])
@api_view(['GET', 'POST', 'PUT'])
def category_api_view(request):
    if request.method == "POST":
        data = request.data 
        serialilzer = CategorySerializer(data)
        if serialilzer.is_valid(raise_exception=True):
            serialilzer.save()
            return Response(serialilzer.data, status=status.HTTP_201_CREATED)
        return Response(serialilzer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "GET":
        category = Category.objects.all()
        serialilzer = CategorySerializer(category, many=True)
        return Response(serialilzer.data, status=status.HTTP_200_OK)


class CategoryViewSet(ModelViewSet):
    throttle_classes = [CategoryThrottle]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = [AuthorPermission] #permissions.AllowAny, permissions.IsAdminUser, permissions.IsAuthenticated permissions.IsAuthenticatedOrReadOnly
    
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