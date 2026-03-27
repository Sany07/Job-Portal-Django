from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

class EmployeeProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee_profile')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    bio = models.TextField(blank=True)
    skills = TaggableManager(blank=True)

    def __str__(self):
        return f"Profile for {self.user.email}"

class EmployerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employer_profile')
    company_website = models.URLField(blank=True)
    company_logo = models.ImageField(upload_to='logos/', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Employer Profile for {self.user.email}"
