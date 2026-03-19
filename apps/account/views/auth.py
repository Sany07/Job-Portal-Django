from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from account.forms import EmployerRegistrationForm, EmployeeRegistrationForm, UserLoginForm


def get_success_url(request):
    """
    Handle Success Url After LogIN
    """
    if 'next' in request.GET and request.GET['next'] != '':
        return request.GET['next']
    return reverse('jobapp:dashboard')


def employee_registration(request):
    """
    Handle Employee Registration
    """
    form = EmployeeRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your account was successfully created! Please log in.')
        return redirect('account:login')
    context = {'form': form}
    return render(request, 'account/employee-registration.html', context)


def employer_registration(request):
    """
    Handle Employee Registration
    """
    form = EmployerRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Employer account was successfully created! Please log in.')
        return redirect('account:login')
    context = {'form': form}
    return render(request, 'account/employer-registration.html', context)


def user_login_view(request):
    """
    Provides users to logIn
    """
    form = UserLoginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST' and form.is_valid():
        auth.login(request, form.get_user())
        return HttpResponseRedirect(get_success_url(request))

    context = {'form': form}
    return render(request, 'account/login.html', context)


def user_logout_view(request):
    """
    Provide the ability to logout
    """
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('account:login')

