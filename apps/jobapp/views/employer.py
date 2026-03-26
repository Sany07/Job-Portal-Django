from django.contrib import messages
from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from jobapp.forms import JobEditForm, JobForm
from jobapp.models import Applicant, Category, Job
from jobapp.permission import EmployerRequiredMixin
from jobapp.services import toggle_job_status

User = get_user_model()


class CreateJobView(EmployerRequiredMixin, CreateView):
    """Employer creates a new job post."""
    model = Job
    form_class = JobForm
    template_name = 'jobapp/post-job.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        form.save_m2m()
        messages.success(self.request, 'You are successfully posted your job! Please wait for review.')
        return redirect(reverse_lazy('jobapp:single-job', kwargs={'id': instance.id}))


class JobEditView(EmployerRequiredMixin, UpdateView):
    """Employer edits an existing job post."""
    model = Job
    form_class = JobEditForm
    template_name = 'jobapp/job-edit.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, 'Your Job Post Was Successfully Updated!')
        return redirect(reverse_lazy('jobapp:single-job', kwargs={'id': instance.id}))


class DeleteJobView(EmployerRequiredMixin, DeleteView):
    """Employer deletes a job post."""
    model = Job
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('jobapp:dashboard')

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)

    def form_valid(self, form):
        # Invalidate cache before deleting
        cache.delete(str(self.get_object().id))
        messages.success(self.request, 'Your Job Post was successfully deleted!')
        return super().form_valid(form)


class MakeCompleteJobView(EmployerRequiredMixin, View):
    """Employer marks a job as closed. (Custom action — kept as View subclass)"""
    def post(self, request, id):
        try:
            toggle_job_status(request.user.id, id)
            messages.success(request, 'Your Job was marked closed!')
        except Exception:
            messages.error(request, 'Something went wrong!')
        return redirect('jobapp:dashboard')

    # Allow GET as well for compatibility with existing links
    def get(self, request, id):
        return self.post(request, id)


class AllApplicantsView(EmployerRequiredMixin, ListView):
    """Employer views all applicants for a specific job."""
    template_name = 'jobapp/all-applicants.html'
    context_object_name = 'all_applicants'

    def get_queryset(self):
        return Applicant.objects.filter(job_id=self.kwargs['id']).select_related('user', 'job')


class ApplicantDetailsView(EmployerRequiredMixin, DetailView):
    """Employer views details of a specific applicant."""
    model = User
    template_name = 'jobapp/applicant-details.html'
    context_object_name = 'applicant'
    pk_url_kwarg = 'id'


class UpdateApplicantStatusView(EmployerRequiredMixin, View):
    """Employer updates the status of an application (Accepted/Rejected)."""
    def post(self, request, id):
        applicant = get_object_or_404(Applicant, id=id)
        # Ensure the employer owns the job
        if applicant.job.user != request.user:
            messages.error(request, 'You are not authorized to perform this action.')
            return redirect('jobapp:dashboard')
        
        status = request.POST.get('status')
        if status in ['accepted', 'rejected']:
            applicant.status = status
            applicant.save()
            messages.success(request, f'Applicant has been {status}!')
        else:
            messages.error(request, 'Invalid status.')
            
        return redirect('jobapp:applicants', id=applicant.job.id)



