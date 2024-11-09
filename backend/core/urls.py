
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('produits.routers')),
    path('', include('core.doc_urls')),
    path('login/', obtain_auth_token, name='login')
]
