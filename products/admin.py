from django.contrib import admin
from .models import Category, Brand, Gender, Product, Review

# Register models to admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'friendly_name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display = ('name', 'friendly_name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):

    list_display = ('name', 'friendly_name')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'sku',
        'name',
        'brand',
        'category',
        'price',
        'gender',
    )

    ordering = ('sku',)

    list_filter = ('brand',)
    search_fields = ('brand', 'gender')


admin.site.register(Review)
