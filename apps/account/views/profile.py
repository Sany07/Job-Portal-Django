from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from account.forms import EmployeeProfileEditForm
from account.models import User
from jobapp.permission import EmployeeRequiredMixin


class EmployeeEditProfileView(EmployeeRequiredMixin, UpdateView):
    """Employee updates their own profile."""
    model = User
    form_class = EmployeeProfileEditForm
    template_name = 'account/employee-edit-profile.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        # Employees can only edit their own profile
        return User.objects.filter(id=self.request.user.id)

    def get_success_url(self):
        return reverse_lazy('account:edit-profile', kwargs={'id': self.object.id})

    def form_valid(self, form):
        messages.success(self.request, 'Your Profile Was Successfully Updated!')
        return super().form_valid(form)



