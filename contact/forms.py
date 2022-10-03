"""
Contact form
"""
from django.forms import ModelForm
from .models import ContactUs


class ContactUsForm(ModelForm):
    """
    The form is for user to contact the shop owner.
    """
    class Meta:
        """Meta class for the form"""
        model = ContactUs
        fields = [
            'full_name',
            'email',
            'message',
        ]
