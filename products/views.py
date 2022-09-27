"""
Products app views
"""
from decimal import Decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Review
from .forms import AddToCartForm, SIZE_CHOICES, ProductForm, ReviewForm


# pylint: disable=no-member


def all_products(request):
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
                messages.error(
                    request,
                    "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query
            ) | Q(description__icontains=query)
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

    reviews = product.reviews.all()
    form = AddToCartForm()

    if product.size:
        reduction = Decimal(1)
        prices = []
        for size in SIZE_CHOICES:
            price = product.price / reduction
            new_price = round(price, 2)
            prices.append(new_price)
            reduction += Decimal(.30)

    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST or None)

        if request.user.is_authenticated and review_form.is_valid():
            review_form.instance.user = request.user
            review = review_form.save(commit=False)
            review.product = product
            review.save()

            messages.success(request, 'Successfully added review!')

            if product.rating:
                product.rating = (product.rating)
            else:
                product.rating = review.star_rating
            product.save()

            return redirect(reverse('product_detail', args=[product.id]))

    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'prices': prices,
        'form': form,
        'reviews': reviews,
        'review_form': review_form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ To edit a product by the store owner / admin """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ To delete a product by the store owner / admin """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """
    To add a review.
    """
    product = get_object_or_404(Product, pk=product_id)
    review = Review.objects.all()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST or None)
        if request.user.is_authenticated and review_form.is_valid():
            review_form.instance.user = request.user
            review = review_form.save(commit=False)
            review.product = product
            review.save()

            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            review_form = ReviewForm()

        context = {
            'product': product,
            'review_form': review_form,
            'review': review,
        }
        return render(request, 'products/product_detail.html', context)

    else:
        return redirect('accounts/login.html')


@login_required()
def delete_review(request, review_id):
    """
    To delete the review on a specific product.
    """
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_id)
        product = review.product
        if request.user == review.user:
            review.delete()
            messages.success(request, 'Successfully deleted review!')

    return redirect(reverse('product_detail', args=[product.id]))
