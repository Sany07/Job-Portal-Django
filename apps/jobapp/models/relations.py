from django.contrib.auth import get_user_model
from django.db import models

from core.models import SoftDeleteModel, TimeStampedModel
from .job import Job

User = get_user_model()

STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
)


class Applicant(TimeStampedModel, SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.job.title}"


class BookmarkJob(TimeStampedModel, SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return self.job.title

