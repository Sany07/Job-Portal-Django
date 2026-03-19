from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy

from account.forms import EmployeeProfileEditForm
from account.models import User
from jobapp.permission import user_is_employee


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employee
def employee_edit_profile(request, id):
    """
    Handle Employee Profile Update Functionality
    """
    user = get_object_or_404(User, id=id)
    form = EmployeeProfileEditForm(request.POST or None, instance=user)
    if form.is_valid():
        form = form.save()
        messages.success(request, 'Your Profile Was Successfully Updated!')
        return redirect(reverse("account:edit-profile", kwargs={'id': form.id}))
    context = {'form': form}
    return render(request, 'account/employee-edit-profile.html', context)

