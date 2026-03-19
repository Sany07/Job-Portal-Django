from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy

from jobapp.forms import JobEditForm, JobForm
from jobapp.models import Applicant, Category, Job
from jobapp.permission import user_is_employer
from jobapp.services import delete_user_job, toggle_job_status

User = get_user_model()


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employer
def create_job_view(request):
    """
    Provide the ability to create job post
    """
    form = JobForm(request.POST or None)
    user = get_object_or_404(User, id=request.user.id)
    categories = Category.objects.all()

    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.user = user
        instance.save()
        form.save_m2m()
        messages.success(request, 'You are successfully posted your job! Please wait for review.')
        return redirect(reverse("jobapp:single-job", kwargs={'id': instance.id}))

    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'jobapp/post-job.html', context)


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employer
def delete_job_view(request, id):
    if delete_user_job(request.user.id, id):
        messages.success(request, 'Your Job Post was successfully deleted!')
    return redirect('jobapp:dashboard')


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employer
def make_complete_job_view(request, id):
    try:
        toggle_job_status(request.user.id, id)
        messages.success(request, 'Your Job was marked closed!')
    except Exception:
        messages.success(request, 'Something went wrong !')
    return redirect('jobapp:dashboard')


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employer
def all_applicants_view(request, id):
    all_applicants = Applicant.objects.filter(job=id)
    context = {'all_applicants': all_applicants}
    return render(request, 'jobapp/all-applicants.html', context)


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employer
def applicant_details_view(request, id):
    applicant = get_object_or_404(User, id=id)
    context = {'applicant': applicant}
    return render(request, 'jobapp/applicant-details.html', context)


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employer
def job_edit_view(request, id):
    """
    Handle Job Update
    """
    job = get_object_or_404(Job, id=id, user=request.user.id)
    categories = Category.objects.all()
    form = JobEditForm(request.POST or None, instance=job)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Your Job Post Was Successfully Updated!')
        return redirect(reverse("jobapp:single-job", kwargs={'id': instance.id}))
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'jobapp/job-edit.html', context)

