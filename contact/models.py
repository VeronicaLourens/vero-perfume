"""
Contact us models
"""
from django.db import models
from django.core.validators import RegexValidator

alpha_only = RegexValidator(
    r'^[a-zA-Z ]*$',
    'Only alpha[a-zA-Z] characters are allowed.'
)


class ContactUs(models.Model):
    """
    To contact the shop owner.
    """
    full_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        validators=[alpha_only]
        
    )
    email = models.EmailField()
    message = models.TextField(
        max_length=250,
        null=False,
        blank=False
    )
    date_sent = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        """
        Meta data for the contact.
        """
        ordering = ('-date_sent',)

    def __str__(self):
        return f'{self.email}'
