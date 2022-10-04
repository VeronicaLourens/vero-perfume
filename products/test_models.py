"""
To test products app models
"""
from django.test import TestCase
from .models import Product, Category, Brand

# pylint: disable=no-member


class TestCategoryModel(TestCase):
    """
    To test category model
    """
    def setUp(self):
        """Set up test"""
        self.category = Category.objects.create(name='perfume')

    def test_category_model_instance(self):
        """To test category model"""
        data = self.category
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        """To test category name"""
        data = self.category
        self.assertEquals(str(data), 'perfume')


class TestBrandModel(TestCase):
    """
    To test brand model
    """
    def setUp(self):
        """To set up test"""
        self.brand = Brand.objects.create(name='Veronica')

    def test_brand_model_instance(self):
        """To test brand model"""
        data = self.brand
        self.assertTrue(isinstance(data, Brand))

    def test_brand_model_name(self):
        """To test brand name"""
        data = self.brand
        self.assertEquals(str(data), 'Veronica')


class TestProductModel(TestCase):
    """
    To test product models
    """
    def setUp(self):
        """
        To create test
        """
        self.product = Product.objects.create(
            sku='Vero999999999',
            name='Lourens',
            rating=5,
            price=200,
            gender='gender',
            description='Awesome perfume for everyone',
            notes='roses and spring water',
        )

    def test_product_model_instance(self):
        """To test product model"""
        data = self.product
        self.assertTrue(isinstance(data, Product))

    def test_product_model_name(self):
        """To test product name"""
        data = self.product
        self.assertEquals(str(data), 'Lourens')

    def test_product_brand(self):
        """To test product brand"""
        data = self.product
        self.assertEquals(str(data), 'Lourens')
