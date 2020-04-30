from django.urls import path
from jobapp import views

app_name = "jobapp"


urlpatterns = [

    path('', views.home_view, name='home'),
    path('job/create/', views.create_job_View, name='create-job'),
    path('job/<int:id>/', views.single_job_view, name='single-job'),
    path('about/', views.single_job_view, name='about'),
    path('contact/', views.single_job_view, name='contact'),


]
