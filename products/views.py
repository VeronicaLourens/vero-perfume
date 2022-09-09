from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category, Brand, Gender
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from decimal import Decimal
from .forms import AddToCartForm, SIZE_CHOICES


def products(request):
    """
    To render all products page.
    Sorting, filtering and search queries.
    """

    products = Product.objects.all()
    query = None
    categories = None
    brands = None
    sort = None
    direction = None
    gender = None

    if request.GET:

        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            products = products.filter(gender__in=gender)
            gender = Category.objects.filter(name__in=gender)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            brands = Category.objects.filter(name__in=brands)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_brands': brands,
        'gender': gender,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ To render the product detail page."""

    product = get_object_or_404(Product, pk=product_id)
    form = AddToCartForm()

    if product.size:
        reduction = Decimal(1)
        prices = []
        for size in SIZE_CHOICES:
            price = product.price / reduction
            new_price = round(price, 2)
            prices.append(new_price)
            reduction += Decimal(.30)

    context = {
        'product': product,
        'prices': prices,
        'form': form, 
    }

    return render(request, 'products/product_detail.html', context)

