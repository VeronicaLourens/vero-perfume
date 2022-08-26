from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    To calculate the subtotal in the cart.
    """
    return price * quantity

