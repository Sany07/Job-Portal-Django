from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

from jobapp.forms import *
from jobapp.models import *
def home_view(request):

    return render(request,'jobapp/index.html')



@login_required(login_url=reverse_lazy('account:login'))
def create_job_View(request):

    form = JobForm(request.POST or None)

    user = get_object_or_404(User, id = request.user.id)
    categories = Category.objects.all()

    if request.method == 'POST':

        if form.is_valid():

            instance=form.save(commit=False)
            instance.user=user
            instance.save()
            #for save tag 
            form.save_m2m()

            return redirect(reverse("jobapp:single-job", kwargs={
                                    'id': instance.id
            }))
    
    context = {
        'form': form,
        'categories':categories
    }
    return render(request,'jobapp/post-job.html', context)




def single_job_view(request, id):

    job = get_object_or_404(Job, id=id)
    related_job = job.tags.similar_objects()
    
 
    context = {
        'job': job,
        'related_job':related_job,
        'total':len(related_job)
        
    }
    return render(request,'jobapp/job-single.html', context)