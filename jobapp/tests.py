from django.test import TestCase
from django.urls import reverse


class SmokeTests(TestCase):
    def test_home_status_code(self):
        """The homepage should return HTTP 200."""
        response = self.client.get(reverse('jobapp:home'))
        self.assertEqual(response.status_code, 200)
