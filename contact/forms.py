from django import forms
from django.forms import ModelForm
from .models import ContactUs


class ContactUsForm(ModelForm):
    """
    The form is for user to contact the shop owner.
    """
    class Meta:
        model = ContactUs
        fields = [
            'full_name',
            'email',
            'message',
        ]