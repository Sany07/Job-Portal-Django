from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from django.db.models import F
from jobapp.models import Job
from jobapp.selectors import get_listed_jobs, search_jobs

User = get_user_model()


def home_view(request):
    """
    Home page — kept as FBV due to AJAX + stats logic.
    """
    published_jobs = Job.objects.filter(is_published=True).order_by('-updated_at')
    jobs = published_jobs.filter(is_closed=False)
    total_candidates = User.objects.filter(role='employee').count()
    total_companies = User.objects.filter(role='employer').count()
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        job_lists = []
        for job_list in page_obj.object_list.values():
            job_lists.append(job_list)
        data = {
            'job_lists': job_lists,
            'current_page_no': page_obj.number,
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
            'no_of_page': paginator.num_pages,
            'prev_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        }
        return JsonResponse(data)

    # Cache stats for 15 minutes
    stats = cache.get('home_stats')
    if not stats:
        stats = {
            'total_candidates': User.objects.filter(role='employee').count(),
            'total_companies': User.objects.filter(role='employer').count(),
            'total_jobs': jobs.count(),
            'total_completed_jobs': published_jobs.filter(is_closed=True).count(),
        }
        cache.set('home_stats', stats, 60 * 15)

    context = {
        'total_candidates': stats['total_candidates'],
        'total_companies': stats['total_companies'],
        'total_jobs': stats['total_jobs'],
        'total_completed_jobs': stats['total_completed_jobs'],
        'page_obj': page_obj,
    }
    return render(request, 'jobapp/index.html', context)


class JobListView(ListView):
    """All published open jobs."""
    template_name = 'jobapp/job-list.html'
    context_object_name = 'page_obj'
    paginate_by = 12

    def get_queryset(self):
        return get_listed_jobs()


class SingleJobView(DetailView):
    """Single job detail page with related jobs and caching."""
    template_name = 'jobapp/job-single.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        job_id = self.kwargs['id']
        
        # Increment views_count safely in DB
        Job.objects.filter(id=job_id).update(views_count=F('views_count') + 1)
        
        job = cache.get(job_id)
        if not job:
            job = get_object_or_404(Job, id=job_id)
            cache.set(job_id, job, 60 * 15)
        else:
            # Refresh views_count in cached object
            job.views_count += 1
            cache.set(job_id, job, 60 * 15)
            
        return job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_job_list = self.object.tags.similar_objects()
        paginator = Paginator(related_job_list, 5)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        context['total'] = len(related_job_list)
        return context


class SearchResultView(ListView):
    """Job search results with multiple filter fields."""
    template_name = 'jobapp/result.html'
    context_object_name = 'page_obj'
    paginate_by = 10

    def get_queryset(self):
        return search_jobs(
            title_or_company=self.request.GET.get('job_title_or_company_name'),
            location=self.request.GET.get('location'),
            job_type=self.request.GET.get('job_type'),
        )



