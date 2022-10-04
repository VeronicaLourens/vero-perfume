from django.test import TestCase
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import get_object_or_404


class TestProfileViews(TestCase):
    """
    To set up test profile page
    """
    def setUp(self):
        """To set up a test user"""
        username = 'username'
        email = 'test@user.com'
        password = 'testpassword'
        user = get_user_model()
        self.user = user.objects.create_user(
            username=username,
            email=email,
            password=password
        )

    def test_profile_page(self):
        """To test profile page"""
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 404)
