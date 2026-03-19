from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from jobapp.forms import JobApplyForm, JobBookmarkForm
from jobapp.models import Applicant, BookmarkJob, Job
from jobapp.permission import user_is_employee
from jobapp.services import remove_bookmark


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employee
def apply_job_view(request, id):
    form = JobApplyForm(request.POST or None)
    user = request.user
    job = get_object_or_404(Job, id=id)

    applicant_exists = Applicant.objects.filter(user=user, job=job).exists()
    if request.method == 'POST':
        if applicant_exists:
            messages.error(request, 'You already applied for the Job!')
        elif form.is_valid():
            Applicant.objects.create(user=user, job=job)
            messages.success(request, 'You have successfully applied for this job!')
        return redirect(reverse("jobapp:single-job", kwargs={'id': id}))

    return redirect(reverse("jobapp:single-job", kwargs={'id': id}))


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employee
def delete_bookmark_view(request, id):
    if remove_bookmark(request.user.id, id):
        messages.success(request, 'Saved Job was successfully deleted!')
    return redirect('jobapp:dashboard')


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employee
def job_bookmark_view(request, id):
    form = JobBookmarkForm(request.POST or None)
    user = request.user
    job = get_object_or_404(Job, id=id)

    bookmark_exists = BookmarkJob.objects.filter(user=user, job=job).exists()
    if request.method == 'POST':
        if bookmark_exists:
            messages.error(request, 'You already saved this Job!')
        elif form.is_valid():
            BookmarkJob.objects.create(user=user, job=job)
            messages.success(request, 'You have successfully save this job!')
        return redirect(reverse("jobapp:single-job", kwargs={'id': id}))

    return redirect(reverse("jobapp:single-job", kwargs={'id': id}))

