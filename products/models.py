from django.db import models

class Category(models.Model):
    """
    To create product's catogory.
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
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
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    To create product with the product details.
    """

    MEN = 'Men'
    WOMEN = 'Women'

    GENDER_CHOICES = [
        (MEN, 'Men'),
        (WOMEN, 'Women')
    ]

    SIZE_CHOICES = [
        ('30ml', '30ml'),
        ('50ml', '50ml'),
        ('75ml', '75ml'),
        ('100ml', '100ml'),

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

    size = models.CharField(
        choices=SIZE_CHOICES,
        max_length=12,
        default=''
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
    )
    image = models.ImageField(
        null=True, blank=True
    )

    def __str__(self):
        return self.name
