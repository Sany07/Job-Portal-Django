from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy

from jobapp.models import Applicant, BookmarkJob, Job


@login_required(login_url=reverse_lazy('account:login'))
def dashboard_view(request):
    """
    Handle Dashboard View
    """
    jobs = []
    savedjobs = []
    appliedjobs = []
    total_applicants = {}

    if request.user.role == 'employer':
        jobs = Job.objects.filter(user=request.user.id)
        for job in jobs:
            count = Applicant.objects.filter(job=job.id).count()
            total_applicants[job.id] = count

    if request.user.role == 'employee':
        savedjobs = BookmarkJob.objects.filter(user=request.user.id)
        appliedjobs = Applicant.objects.filter(user=request.user.id)

    context = {
        'jobs': jobs,
        'savedjobs': savedjobs,
        'appliedjobs': appliedjobs,
        'total_applicants': total_applicants,
    }
    return render(request, 'jobapp/dashboard.html', context)

