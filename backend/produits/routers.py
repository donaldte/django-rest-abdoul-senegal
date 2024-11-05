# defaultRouter 
from rest_framework.routers import DefaultRouter
from produits.api.api import CategoryViewSet, ProductViewSet

router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')

urlpatterns = router.urls