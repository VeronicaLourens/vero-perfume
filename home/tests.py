from django.test import TestCase


class TestHomeViews(TestCase):
    """
    To test the home page views
    """
    def test_home_page(self):
        """
        To check the home page
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
