from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView, View, DetailView

from account.forms import EmployeeProfileEditForm, EmployeeProfileForm, EmployerProfileForm
from account.models import User, EmployeeProfile, EmployerProfile
from jobapp.permission import EmployeeRequiredMixin

class EmployeeEditProfileView(EmployeeRequiredMixin, View):
    """Employee updates their own user and profile data."""
    template_name = 'account/employee-edit-profile.html'

    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        if user != request.user:
            return redirect('jobapp:home')
        
        user_form = EmployeeProfileEditForm(instance=user)
        profile, created = EmployeeProfile.objects.get_or_create(user=user)
        profile_form = EmployeeProfileForm(instance=profile)
        
        return render(request, self.template_name, {
            'form': user_form,
            'profile_form': profile_form
        })

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        if user != request.user:
            return redirect('jobapp:home')
            
        user_form = EmployeeProfileEditForm(request.POST, instance=user)
        profile, created = EmployeeProfile.objects.get_or_create(user=user)
        profile_form = EmployeeProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile Was Successfully Updated!')
            return redirect('account:edit-profile', id=user.id)
            
        return render(request, self.template_name, {
            'form': user_form,
            'profile_form': profile_form
        })

class EmployerEditProfileView(View):
    """Employer updates their own user and profile data."""
    template_name = 'account/employer-edit-profile.html'

    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        if user != request.user or user.role != 'employer':
            return redirect('jobapp:home')
        
        user_form = EmployeeProfileEditForm(instance=user) # Can reuse or create specialized
        profile, created = EmployerProfile.objects.get_or_create(user=user)
        profile_form = EmployerProfileForm(instance=profile)
        
        return render(request, self.template_name, {
            'form': user_form,
            'profile_form': profile_form
        })

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        if user != request.user or user.role != 'employer':
            return redirect('jobapp:home')
            
        user_form = EmployeeProfileEditForm(request.POST, instance=user)
        profile, created = EmployerProfile.objects.get_or_create(user=user)
        profile_form = EmployerProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Company Profile Was Successfully Updated!')
            return redirect('account:edit-profile', id=user.id)
            
        return render(request, self.template_name, {
            'form': user_form,
            'profile_form': profile_form
        })
class CandidateProfileView(DetailView):
    """View candidate profile."""
    model = EmployeeProfile
    template_name = 'account/candidate-profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(EmployeeProfile, user_id=self.kwargs.get('id'))

class EmployerProfileView(DetailView):
    """View employer profile."""
    model = EmployerProfile
    template_name = 'account/employer-profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(EmployerProfile, user_id=self.kwargs.get('id'))

