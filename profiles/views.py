from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, ProfileDeleteForm
from checkout.models import Order


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
            messages.success(request, 'Your profile has been updated successfully!')
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
    To delete the user profile and associated data from the database.
    """
    if request.method == 'POST':
        delete_profile = ProfileDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()

        messages.success(request, f'Your profile has been deleted!')
        return redirect('home')

    else:
        delete_profile = ProfileDeleteForm(instance=request.user)

    context = {
        'delete_profile': delete_profile,
        'title': 'UserProfile'
    }

    return render(request, 'profiles/delete_profile.html', context)


def wishlist(request):
    """
    To render wishlist.
    """
    wishlist = None
    try:
        wishlist = WishList.objects.get(user=request.user)
    except WishList.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, profiles/wishlist.html, context)

