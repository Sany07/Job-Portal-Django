from django.contrib.sitemaps import Sitemap
from jobapp.models import Job

class JobSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Job.objects.filter(is_published=True, is_closed=False).order_by('-created_at')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        from django.urls import reverse
        return reverse('jobapp:single-job', kwargs={'id': obj.id})
