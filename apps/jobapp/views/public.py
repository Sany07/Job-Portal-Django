from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from jobapp.models import Job
from jobapp.selectors import get_listed_jobs, search_jobs

User = get_user_model()


def home_view(request):
    published_jobs = Job.objects.filter(is_published=True).order_by('-timestamp')
    jobs = published_jobs.filter(is_closed=False)
    total_candidates = User.objects.filter(role='employee').count()
    total_companies = User.objects.filter(role='employer').count()
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        job_lists = []
        job_objects_list = page_obj.object_list.values()
        for job_list in job_objects_list:
            job_lists.append(job_list)

        next_page_number = page_obj.next_page_number() if page_obj.has_next() else None
        prev_page_number = page_obj.previous_page_number() if page_obj.has_previous() else None

        data = {
            'job_lists': job_lists,
            'current_page_no': page_obj.number,
            'next_page_number': next_page_number,
            'no_of_page': paginator.num_pages,
            'prev_page_number': prev_page_number,
        }
        return JsonResponse(data)

    context = {
        'total_candidates': total_candidates,
        'total_companies': total_companies,
        'total_jobs': len(jobs),
        'total_completed_jobs': len(published_jobs.filter(is_closed=True)),
        'page_obj': page_obj,
    }
    return render(request, 'jobapp/index.html', context)


def job_list_View(request):
    """
    Handle Job List View
    """
    job_list = get_listed_jobs()
    paginator = Paginator(job_list, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'jobapp/job-list.html', context)


def single_job_view(request, id):
    """
    Provide the ability to view job details
    """
    if cache.get(id):
        job = cache.get(id)
    else:
        job = get_object_or_404(Job, id=id)
        cache.set(id, job, 60 * 15)
    related_job_list = job.tags.similar_objects()

    paginator = Paginator(related_job_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'job': job,
        'page_obj': page_obj,
        'total': len(related_job_list),
    }
    return render(request, 'jobapp/job-single.html', context)


def search_result_view(request):
    """
    User can search job with multiple fields
    """
    job_list = search_jobs(
        title_or_company=request.GET.get('job_title_or_company_name'),
        location=request.GET.get('location'),
        job_type=request.GET.get('job_type'),
    )

    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'jobapp/result.html', context)

