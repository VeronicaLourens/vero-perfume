from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.dispatch import receiver
from products.models import Product

# pylint: disable=no-member

alpha_only = RegexValidator(
    r'^[a-zA-Z ]*$',
    'Only alpha[a-zA-Z] characters are allowed.'
)

number_only = RegexValidator(
    r'^[0-9]*$',
    'Only numbers are allowed.'
)


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(
        User,
        null=True,
        on_delete=models.
        CASCADE
    )
    default_full_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        validators=[alpha_only]
    )
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[number_only]
    )
    default_street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_city = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    default_county = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    default_postcode = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        validators=[number_only]
    )
    default_country = CountryField(
        blank_label='Country',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile.
    """
    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()


class WishList(models.Model):
    """
    To save products on user's wishlist.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField(
        Product,
        through='WishListItem',
        related_name='product_wishlists'
    )

    def __str__(self):
        return f'Wishlist ({self.user})'


class WishListItem(models.Model):
    """
    This model is for user to add products to the wishlist.
    """
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    wishlist = models.ForeignKey(
        WishList,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product.name
