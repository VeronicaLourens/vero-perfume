"""Products app models"""
from django.db import models
from django.contrib.auth.models import User

# pylint: disable=no-member


class Category(models.Model):
    """
    To create product's catogory.
    """

    class Meta:
        """Category name"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        """Category friendly name"""
        return self.friendly_name


class Brand(models.Model):
    """
    To create product's brand.
    """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        """Brand name"""
        return self.friendly_name


class Gender(models.Model):
    """
    To create product's gender.
    """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        """Gender name"""
        return self.friendly_name


class Product(models.Model):
    """
    To create product with the product details.
    """
    MEN = 'Men'
    WOMEN = 'Women'
    UNISEX = 'Unisex'

    GENDER_CHOICES = [
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (UNISEX, 'Unisex')
    ]

    sku = models.CharField(
        max_length=254,
        null=True, blank=True
    )
    name = models.CharField(
        max_length=254
        )
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    brand = models.ForeignKey(
        'Brand',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    has_sizes = models.BooleanField(
        default=True,
        null=True,
        blank=True
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=24,
        default=''
    )
    description = models.TextField()
    notes = models.TextField(null=True, blank=True)

    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    """
    To create a review.
    """
    STAR_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=25,
        null=False,
        blank=False
    )
    content = models.TextField(
        max_length=250,
        null=False,
        blank=False
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    star_rating = models.IntegerField(
        choices=STAR_CHOICES,
        default=5,
    )
    approved = models.BooleanField(default=False)

    class Meta:
        """Review"""
        ordering = ['id']

    def __str__(self):
        return f'{self.title}'
