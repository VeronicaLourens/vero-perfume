from django.shortcuts import render, get_object_or_404
from .models import Product

def products(request):
    """ To render all products page."""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)



def product_detail(request, product_id):
    """ To render the product detail page."""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

