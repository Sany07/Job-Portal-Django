from django.test import TestCase, Client
from django.urls import reverse
from django.core.cache import cache
from django.contrib.auth import get_user_model
from jobapp.models import Job, Category

User = get_user_model()

class JobappViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test@example.com', password='password', role='employer')
        self.category = Category.objects.create(name='Test Category')
        self.job = Job.objects.create(
            user=self.user,
            title='Original Title',
            description='Description',
            location='Location',
            job_type='1',
            category=self.category,
            last_date='2026-12-31',
            is_published=True
        )

    def test_single_job_view_reflects_update(self):
        """Verify that the detail view shows the updated title immediately (cache invalidation)."""
        url = reverse('jobapp:single-job', kwargs={'id': self.job.id})
        
        # 1. First request to populate cache
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Original Title')

        # 2. Update the job title
        self.job.title = 'Updated Title'
        self.job.save()

        # 3. Second request - should NOT show the old title from cache
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Updated Title')
        self.assertNotContains(response, 'Original Title')

