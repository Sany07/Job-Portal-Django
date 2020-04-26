from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from jobapp.forms import *
from jobapp.models import *

# Create your views here.

def home(request):

    return render(request,'jobapp/index.html')

@login_required(login_url=reverse_lazy('account:login'))
def JobCreateView(request):
    form = JobForm(request.POST or None)
    categories = Category.objects.all() 
    user=get_object_or_404(User,id=request.user.id)

    if request.method=='POST':

        if form.is_valid:

            instance=form.save(commit=False)
            instance.user = user

            instance.save()
           
            return redirect(reverse("jobapp:job-Details" ,kwargs={
                    'id':form.instance.id
            }))

            print(instance)
    context={
        
            'form':form ,
            'categories':categories
        }

    return render(request,'jobapp/post-job.html',context)



def JobDetailsView(request, id):

    job = get_object_or_404(Job, id=id)
    
    context ={

        'job':job
    }
    return render(request,'jobapp/job-single.html',context)