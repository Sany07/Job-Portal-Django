from django.contrib import auth, messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from account.forms import EmployerRegistrationForm, EmployeeRegistrationForm, UserLoginForm


class UserLoginView(LoginView):
    """
    Email-based login using Django's built-in LoginView.
    Redirects to dashboard after login.
    """
    form_class = UserLoginForm
    template_name = 'account/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.GET.get('next') or self.request.POST.get('next')
        if next_url:
            return next_url
        return reverse('jobapp:dashboard')


class UserLogoutView(LogoutView):
    """Logs out the user and redirects to login page."""
    next_page = reverse_lazy('account:login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You are successfully logged out.')
        return super().dispatch(request, *args, **kwargs)


class EmployeeRegistrationView(CreateView):
    """Handles employee (job seeker) registration."""
    form_class = EmployeeRegistrationForm
    template_name = 'account/employee-registration.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your account was successfully created! Please log in.')
        return redirect(self.success_url)


class EmployerRegistrationView(CreateView):
    """Handles employer (company) registration."""
    form_class = EmployerRegistrationForm
    template_name = 'account/employer-registration.html'
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your Employer account was successfully created! Please log in.')
        return redirect(self.success_url)



