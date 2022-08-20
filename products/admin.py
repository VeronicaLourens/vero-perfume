from django.contrib import admin
from .models import Category, Brand, Product

# Register models to admin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name','brand', 'category')
    list_filter = ('name', 'brand')
    search_fields = ('brand', 'gender')
    