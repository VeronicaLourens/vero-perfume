from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, WishList
from .forms import UserProfileForm, ProfileDeleteForm
from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    """
    To render user profile page with user's personal information.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your profile has been updated successfully!'
            )
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, template, context)


def personal_details(request):
    """
    To render the personal details page.
    """
    template = 'profiles/personal_details.html'
    context = {
        'form': UserProfileForm
    }
    return render(request, template, context)


def order_history(request, order_number):
    """
    To render the order list.
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def delete_profile(request):
    """
    To delete the user profile
    and associated data from the database.
    """
    if request.method == 'POST':
        delete_profile = ProfileDeleteForm(
            request.POST,
            instance=request.user
        )
        user = request.user
        user.delete()

        messages.success(request, 'Your profile has been deleted!')
        return redirect('home')

    else:
        delete_profile = ProfileDeleteForm(instance=request.user)

    context = {
        'delete_profile': delete_profile,
        'title': 'UserProfile'
    }

    return render(request, 'profiles/delete_profile.html', context)


@login_required()
def wishlist(request):
    """
    To render wishlist.
    """
    wishlist_items = []
    wishlist_count = 0
    wishlist = request.session.get('wishlist', {})

    try:
        wishlist = WishList.objects.get(user=request.user)
    except Exception as e:
        messages.error(request, 'Sorry, please login to your account first.')
        return HttpResponse(content=e, status=500)
    else:
        wishlist_items = wishlist.products.all()

    context = {
        'wishlist': wishlist,
        'wishlist_items': wishlist_items,
        'wishlist_count': wishlist_count,
    }
    return render(request, 'profiles/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    To add a product to the wishlist.
    """
    product = get_object_or_404(Product, pk=product_id)

    # Create a wishlist for the user if they don't have one
    wishlist, _ = WishList.objects.get_or_create(user=request.user)

    # Add product to the wishlist
    if product in wishlist.products.all():
        messages.error(
            request,
            product.name + ' is already in your wishlist.'
        )
    else:
        wishlist.products.add(product)
        messages.info(
            request,
            'Added ' + product.name + ' to your wishlist.'
        )

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, product_id):
    """
   To remove a product from the wishlist.
    """
    wishlist = WishList.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Remove product from the wishlist
    wishlist.products.remove(product)
    messages.info(
        request,
        product.name + ' was removed from your wishlist.'
    )

    return redirect(request.META.get('HTTP_REFERER'))
