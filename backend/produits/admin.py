from django.contrib import admin

from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    
admin.site.register(Product, ProductAdmin)    
admin.site.register(Category)