from django.urls import path
from account.views import (
    EmployeeEditProfileView,
    EmployerEditProfileView,
    EmployeeRegistrationView,
    EmployerRegistrationView,
    UserLoginView,
    UserLogoutView,
    CandidateProfileView,
    EmployerProfileView,
)

app_name = "account"

urlpatterns = [
    path('employee/register/', EmployeeRegistrationView.as_view(), name='employee-registration'),
    path('employer/register/', EmployerRegistrationView.as_view(), name='employer-registration'),
    path('profile/edit/<int:id>/', EmployeeEditProfileView.as_view(), name='edit-profile'),
    path('employer/profile/edit/<int:id>/', EmployerEditProfileView.as_view(), name='employer-edit-profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('candidate/profile/<int:id>/', CandidateProfileView.as_view(), name='candidate-profile'),
    path('employer/profile/view/<int:id>/', EmployerProfileView.as_view(), name='employer-profile'),
]
