# Generated by Django 3.2 on 2022-10-06 16:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='full_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', 'Only alpha[a-zA-Z] characters are allowed.')]),
        ),
    ]
