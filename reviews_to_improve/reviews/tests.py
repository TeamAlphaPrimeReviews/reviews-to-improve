from django.test import TestCase
from django.test import Client


class TestHomeView(TestCase):
    """Class containing home view tests."""

    def setUp(self):
        """Set up for client creation."""
        self.client = Client()

    def test_home_view_response_is_200_ok(self):
        """Function that tests a response from a GET request to the home view
        url returns an HTTP 200 OK response."""

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_home_view_renders_proper_template(self):
        """Function that tests a response from a GET request to the home view
        renders the correct template used to display the home-page."""

        response = self.client.get('/')

        self.assertTemplateUsed(response, 'index.html')
