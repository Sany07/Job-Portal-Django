from django.db.models import QuerySet
from jobapp.models import Job

def get_listed_jobs() -> QuerySet[Job]:
    """Return all published jobs that are not closed."""
    return Job.objects.select_related('category', 'user').filter(is_published=True, is_closed=False).order_by('-updated_at')

def search_jobs(title_or_company: str | None = None, location: str | None = None, job_type: str | None = None) -> QuerySet[Job]:
    """Search for jobs based on dynamic filters."""
    job_list = Job.objects.select_related('category', 'user').order_by('-updated_at')

    if title_or_company:
        job_list = job_list.filter(title__icontains=title_or_company) | job_list.filter(company_name__icontains=title_or_company)

    if location:
        job_list = job_list.filter(location__icontains=location)

    if job_type:
        job_list = job_list.filter(job_type__iexact=job_type)

    return job_list
