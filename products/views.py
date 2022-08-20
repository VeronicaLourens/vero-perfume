from django.shortcuts import render
from .models import Product

def products(request):
    """ To render all products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
