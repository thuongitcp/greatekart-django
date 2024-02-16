from django.contrib import admin

# Register your models here.
from .models import Product
# from store import models
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',)}
    
admin.site.register(Product, ProductAdmin)