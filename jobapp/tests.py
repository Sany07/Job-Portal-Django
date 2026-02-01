from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class SmokeTests(TestCase):
    def test_home_status_code(self):
        """The homepage should return HTTP 200."""
        response = self.client.get(reverse('jobapp:home'))
        self.assertEqual(response.status_code, 200)
