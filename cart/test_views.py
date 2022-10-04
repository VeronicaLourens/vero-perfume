"""
To test cart views
"""
from django.test import TestCase
from products.models import Product

# pylint: disable=no-member


class TestCartView(TestCase):
    """
    To test the shopping cart views
    """
    def setUp(self):
        """To create a test product"""
        Product.objects.create(
            name='Test name',
            price='180',
            description='A perfect Perfume for everyone',
        )

    def test_cart_page(self):
        """To test the cart page"""
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
