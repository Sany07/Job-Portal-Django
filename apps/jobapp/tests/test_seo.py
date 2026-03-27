from django.test import TestCase
from django.urls import reverse
from jobapp.models import Job, Category
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class SEOTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password', role='employer')
        self.category = Category.objects.create(name='IT')
        self.job = Job.objects.create(
            user=self.user,
            title='Software Engineer',
            description='Test description for SEO.',
            location='New York',
            job_type='1',
            category=self.category,
            company_name='Test Company',
            last_date=datetime.date.today() + datetime.timedelta(days=30),
            is_published=True
        )

    def test_homepage_seo(self):
        response = self.client.get(reverse('jobapp:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>DJobPortal - Find Your Dream Job Today</title>')
        self.assertContains(response, 'meta name="description" content="DJobPortal is the leading job board')

    def test_job_detail_seo(self):
        response = self.client.get(reverse('jobapp:single-job', kwargs={'id': self.job.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Software Engineer at Test Company | DJobPortal</title>')
        self.assertContains(response, 'meta name="description" content="Test description for SEO.')
        self.assertContains(response, '"@type": "JobPosting"')
        self.assertContains(response, '"title": "Software Engineer"')

    def test_sitemap_accessible(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')
        self.assertContains(response, f'/job/{self.job.id}/')

    def test_robots_txt_accessible(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/plain')
        self.assertContains(response, 'User-agent: *')
        self.assertContains(response, 'Sitemap:')
