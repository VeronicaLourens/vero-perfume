"""
Product forms
"""
from django import forms
from django.forms import ModelForm
from .models import Product, Category, Review
from .widgets import CustomClearableFileInput

# pylint: disable=no-member


class AddToCartForm(forms.Form):
    """
    To display product size and pirce.
    """
    quantity = forms.IntegerField(max_value=10, min_value=1)


class ProductForm(forms.ModelForm):
    """
    To manage the product by the shop owner/admin.
    """
    class Meta:
        """Product form"""
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(ModelForm):
    """
    To create review and give rating.
    """
    class Meta:
        """Review form"""
        model = Review
        fields = (
            'title',
            'content',
            'star_rating',
        )
