from django.urls import path
from account.views import (
    employee_edit_profile,
    employee_registration,
    employer_registration,
    user_logIn,
    user_logOut,
)

app_name = "account"

urlpatterns = [

    path('employee/register/', employee_registration, name='employee-registration'),
    path('employer/register/', employer_registration, name='employer-registration'),
    path('profile/edit/<int:id>/', employee_edit_profile, name='edit-profile'),
    path('login/', user_logIn, name='login'),
    path('logout/', user_logOut, name='logout'),
]
