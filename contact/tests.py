from django.test import TestCase
from .forms import ContactUsForm


class TestContactUsForm(TestCase):
    """
    To test contact form
    """
    def test_contact_us_form(self):
        """
        To check the contact us form
        """
        form = ContactUsForm({
            'full_name': 'Test full name',
            'email': 'test@veroperfume.com',
            'message': 'Welcome to Vero Perfume online store!',
        })
        self.assertTrue(form.is_valid())
