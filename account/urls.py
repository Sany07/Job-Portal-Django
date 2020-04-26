from django.urls import path
from account import views

app_name = "account"

urlpatterns = [

    path('employee/register/', views.EmployeeRegistration, name='employee-registration'),
    path('employer/register/', views.EmployeeRegistration, name='employee-registration'),
    path('login/', views.UserLogIn, name='login'),
    path('logout/', views.UserLogOut, name='login-out'),
]
