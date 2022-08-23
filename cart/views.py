from django.shortcuts import render


def view_cart(request):
    """ To render the shopping cart page """

    return render(request, 'cart/cart.html')
    