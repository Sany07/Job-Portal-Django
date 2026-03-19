from django.urls import path
from jobapp.views import (
    all_applicants_view,
    applicant_details_view,
    apply_job_view,
    create_job_view,
    dashboard_view,
    delete_bookmark_view,
    delete_job_view,
    home_view,
    job_bookmark_view,
    job_edit_view,
    job_list_view,
    make_complete_job_view,
    search_result_view,
    single_job_view,
)

app_name = "jobapp"


urlpatterns = [

    path('', home_view, name='home'),
    path('jobs/', job_list_view, name='job-list'),
    path('job/create/', create_job_view, name='create-job'),
    path('job/<int:id>/', single_job_view, name='single-job'),
    path('apply-job/<int:id>/', apply_job_view, name='apply-job'),
    path('bookmark-job/<int:id>/', job_bookmark_view, name='bookmark-job'),
    path('about/', single_job_view, name='about'),
    path('contact/', single_job_view, name='contact'),
    path('result/', search_result_view, name='search_result'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/employer/job/<int:id>/applicants/', all_applicants_view, name='applicants'),
    path('dashboard/employer/job/edit/<int:id>', job_edit_view, name='edit-job'),
    path('dashboard/employer/applicant/<int:id>/', applicant_details_view, name='applicant-details'),
    path('dashboard/employer/close/<int:id>/', make_complete_job_view, name='complete'),
    path('dashboard/employer/delete/<int:id>/', delete_job_view, name='delete'),
    path('dashboard/employee/delete-bookmark/<int:id>/', delete_bookmark_view, name='delete-bookmark'),


]
