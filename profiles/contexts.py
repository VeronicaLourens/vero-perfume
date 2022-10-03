"""
Contexts for the wishlist
"""
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from .models import WishList

# pylint: disable=no-member


def wishlist_context(request):
    """
    To display the content in the wishlist.
    """
    wishlist_items = []
    wishlist_count = 0
    wishlist = request.session.get('wishlist', {})

    if request.user.is_authenticated:
        return {
            'wishlist_count':
            WishList.objects.filter(user=request.user).count()
        }
    else:
        return {
            'wishlist_count': wishlist_count,
        }

    context = {
        'wishlist_items': wishlist_items,
        'wishlist_count': wishlist_count,
    }

    return context
