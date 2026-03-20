from django.contrib.auth import get_user_model
from django.db import models

from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager

User = get_user_model()

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

WORK_MODE = (
    ('remote', 'Remote'),
    ('hybrid', 'Hybrid'),
    ('onsite', 'On-site'),
)

EXPERIENCE_LEVEL = (
    ('entry', 'Entry Level'),
    ('mid', 'Mid Level'),
    ('senior', 'Senior Level'),
    ('lead', 'Lead / Manager'),
)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Job(models.Model):
    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = CKEditor5Field(config_name='extends')
    tags = TaggableManager()
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    work_mode = models.CharField(choices=WORK_MODE, max_length=10, default='onsite')
    experience_level = models.CharField(choices=EXPERIENCE_LEVEL, max_length=10, default='entry')
    category = models.ForeignKey(Category, related_name='Category', on_delete=models.CASCADE)
    salary = models.CharField(max_length=30, blank=True)
    views_count = models.PositiveIntegerField(default=0)
    company_name = models.CharField(max_length=300)
    company_description = CKEditor5Field(config_name='extends', blank=True, null=True)
    url = models.URLField(max_length=200)
    last_date = models.DateField()
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

