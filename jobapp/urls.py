from django.urls import path
from jobapp import views

app_name = "jobapp"

urlpatterns = [

    path('', views.home, name='home'),
    path('employer/jobs/create/', views.JobCreateView, name='create-job'),
    path('jobs/<int:id>/', views.JobDetailsView, name='job-Details'),

]
