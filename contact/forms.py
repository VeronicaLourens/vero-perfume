from django import forms
from django.forms import ModelForm
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    """
    The form is for user to contact the shop owner.
    """
    class Meta:
        model = ContactUs
        fields = [
            'email',
            'contect',
        ]