from django import forms
from .models import Product

SIZE_CHOICES = [
        ('30ml', '30ml'),
        ('50ml', '50ml'),
        ('75ml', '75ml'),
        ('100ml', '100ml'),
    ]


class AddToCartForm(forms.Form):
    """
    To display product size and pirce.
    """

    size = forms.ChoiceField(choices=SIZE_CHOICES)
    quantity = forms.IntegerField(max_value=10, min_value=1)
