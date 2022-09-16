from django.db import models


class ContactUs(models.Model):
    """
    To contact the shop owner.
    """
    email = models.EmailField()
    content = models.TextField(
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
