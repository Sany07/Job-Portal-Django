from django.urls import path
from account import views


urlpatterns = [

    path('employee/register/', views.EmployeeRegistration, name='employee-registration'),
    path('login/', views.UserLogIn, name='login')
]
