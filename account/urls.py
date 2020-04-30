from django.urls import path
from account import views

app_name = "account"

urlpatterns = [

    path('employee/register/', views.employee_registration, name='employee-registration'),
    path('employer/register/', views.employee_registration, name='employer-registration'),
    path('login/', views.user_logIn, name='login'),
    path('logout/', views.user_logOut, name='logout'),
]
