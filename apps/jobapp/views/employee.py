from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, View

from jobapp.forms import JobApplyForm, JobBookmarkForm
from jobapp.models import Applicant, BookmarkJob, Job
from jobapp.permission import EmployeeRequiredMixin
from jobapp.services import remove_bookmark


class ApplyJobView(EmployeeRequiredMixin, View):
    """
    Employee applies to a job. Kept as View (not CreateView)
    because it has custom duplicate-prevention logic.
    """
    def post(self, request, id):
        user = request.user
        job = get_object_or_404(Job, id=id)
        form = JobApplyForm(request.POST)

        if Applicant.objects.filter(user=user, job=job).exists():
            messages.error(request, 'You already applied for the Job!')
        elif form.is_valid():
            Applicant.objects.create(user=user, job=job)
            messages.success(request, 'You have successfully applied for this job!')

        return redirect(reverse('jobapp:single-job', kwargs={'id': id}))

    def get(self, request, id):
        return redirect(reverse('jobapp:single-job', kwargs={'id': id}))


class DeleteBookmarkView(EmployeeRequiredMixin, DeleteView):
    """Employee deletes a saved bookmark."""
    model = BookmarkJob
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('jobapp:dashboard')

    def get_queryset(self):
        return BookmarkJob.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Saved Job was successfully deleted!')
        return super().form_valid(form)


class JobBookmarkView(EmployeeRequiredMixin, View):
    """
    Employee bookmarks a job. Kept as View (not CreateView)
    because it has custom duplicate-prevention logic.
    """
    def post(self, request, id):
        user = request.user
        job = get_object_or_404(Job, id=id)
        form = JobBookmarkForm(request.POST)

        if BookmarkJob.objects.filter(user=user, job=job).exists():
            messages.error(request, 'You already saved this Job!')
        elif form.is_valid():
            BookmarkJob.objects.create(user=user, job=job)
            messages.success(request, 'You have successfully saved this job!')

        return redirect(reverse('jobapp:single-job', kwargs={'id': id}))

    def get(self, request, id):
        return redirect(reverse('jobapp:single-job', kwargs={'id': id}))



