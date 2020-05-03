from django import template

from jobapp.models import Applicant

register = template.Library()


@register.simple_tag(name='is_job_already_applied')
def is_job_already_applied(job, user):
    applied = Applicant.objects.filter(job=job, user=user)
    if applied:
        return True
    else:
        return False
