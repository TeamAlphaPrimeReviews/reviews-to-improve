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

    def test_home_view_response_is_not_404(self):
        """Test a response from GET request is NOT 404 response."""

        response = self.client.get('/')

        self.assertNotEqual(response.status_code, 404)

    def test_home_view_renders_proper_template(self):
        """Function that tests a response from a GET request to the home view
        renders the correct template used to display the home-page."""

        response = self.client.get('/')

        self.assertTemplateUsed(response, 'reviews/startbootstrap-creative-gh-pages/index.html')

    def test_home_view_not_render_improper_template(self):
        """Test GET request renders NOT the incorrect template."""

        response = self.client.get('/')

        self.assertTemplateNotUsed(response, 'reviews/startbootstrap-creative-gh-pages/home.html')

    def test_home_view_response_contains_homepage_elements(self):
        """Function that tests the page rendered contains the elements that the
        home page should contain."""

        response = self.client.get('/')

        el = '<title>Review Improve</title>'
        self.assertIn(el, str(response.content))

    def test_home_view_response_converts_properly_to_bytes(self):
        """Test the byte and unicode conversions in the get request."""

        response = self.client.get('/')

        el = b'<title>Review Improve</title>'
        self.assertIn(el, response.content)

    def test_home_view_static_files_being_loaded_correctly(self):
        """Function that tests the home view being rendered is also rendering
        the correct static files."""

        response = self.client.get('/')

        correct_el = '<link href="https://reviews-to-improve-s3.s3.amazonaws.com/static/reviews/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">'
        self.assertIn(correct_el, str(response.content))

    def test_home_view_static_files_do_not_contain_load_static(self):
        """Function that tests the home view being rendered is also rendering
        the correct static files."""

        response = self.client.get('/')

        incorrect_el = '<link href="{% static "reviews/vendor/bootstrap/css/bootstrap.min.css" %}" rel="stylesheet">'
        self.assertNotIn(incorrect_el, str(response.content))

    def test_home_view_contains_word_about(self):
        """Test home view has a tag with about text to make sure still About link."""

        response = self.client.get('/').content
        el = 'About'
        self.assertInHTML(el, str(response))

    def test_home_view_contains_amazon_aws_s3(self):
        """Test home_view contains the string amazon_aws_s3."""

        response = self.client.get('/').content
        el = '<script src="https://reviews-to-improve-s3.s3.amazonaws.com/static/reviews/js/creative.min.js"></script>'
        self.assertIn(el, str(response))

<<<<<<< HEAD
    def test_about_view_contains_amazon_aws_s3(self):
        response = self.client.get('').content
        el = '<script src="https://reviews-to-improve-s3.s3.amazonaws.com/static/reviews/js/creative.min.js"></script>'
        self.assertIn(el, str(response))

=======

class TestAboutView(TestCase):
    """Class containing about_view tests."""

    def setUp(self):
        """Set up for client creation."""
        self.client = Client()

    def test_about_view_response_is_200_ok(self):
        """Test request to about view url returns 200 response."""

        response = self.client.get('/about/')

        self.assertEqual(response.status_code, 200)

    def test_about_view_response_is_not_404(self):
        """Test request to about view url does NOT return 404."""

        response = self.client.get('/about/')

        self.assertNotEqual(response.status_code, 404)

    def test_about_view_renders_proper_template(self):
        """Test request to about view renders correct template to display on about view."""

        response = self.client.get('/about/')

        self.assertTemplateUsed(response, 'reviews/startbootstrap-full-width-pics-gh-pages/about.html')

    def test_about_view_not_render_improper_template(self):
        """Test GET request renders NOT the incorrect template."""

        response = self.client.get('/about/')

        self.assertTemplateNotUsed(response, 'reviews/startbootstrap-full-width-pics-gh-pages/home.html')

    def test_about_view_response_contains_aboutpage_elements(self):
        """Function that tests the page rendered contains the elements that the
        about page should contain."""

        response = self.client.get('/about/')

        el = '<title>Review Improve - About Us</title>'

        self.assertIn(el, str(response.content))

    def test_about_view_static_files_being_loaded_correctly(self):
        """Function that tests the about view being rendered is also rendering
        the correct static files."""

        response = self.client.get('/about/')

        correct_el = '<link href="https://reviews-to-improve-s3.s3.amazonaws.com/static/reviews/vendor-about/bootstrap/css/bootstrap.min.css" rel="stylesheet">'
        self.assertIn(correct_el, str(response.content))

    # def test_home_view_static_files_do_not_contain_load_static(self):
    #     """Function that tests the home view being rendered is also rendering
    #     the correct static files."""

    #     response = self.client.get('/')

    #     incorrect_el = '<link href="{% static "reviews/vendor/bootstrap/css/bootstrap.min.css" %}" rel="stylesheet">'
    #     self.assertNotIn(incorrect_el, str(response.content))

    # def test_home_view_contains_word_about(self):
    #     """Test home view has a tag with about text to make sure still About link."""

    #     response = self.client.get('/').content
    #     el = 'About'
    #     self.assertInHTML(el, str(response))

    # def test_home_view_contains_amazon_aws_s3(self):
    #     """Test home_view contains the string amazon_aws_s3."""

    #     response = self.client.get('/').content
    #     el = '<script src="https://reviews-to-improve-s3.s3.amazonaws.com/static/reviews/js/creative.min.js"></script>'
    #     self.assertIn(el, str(response))
>>>>>>> 44458d644e243d5f2de735444e3a41fffb2a9ff3
