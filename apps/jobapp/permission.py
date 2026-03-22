from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy


# ── FBV Decorators (kept for backward compatibility) ─────────────────────────

def user_is_employer(function):
    def wrap(request, *args, **kwargs):
        if request.user.role == 'employer':
            return function(request, *args, **kwargs)
        raise PermissionDenied
    return wrap


def user_is_employee(function):
    def wrap(request, *args, **kwargs):
        if request.user.role == 'employee':
            return function(request, *args, **kwargs)
        raise PermissionDenied
    return wrap


# ── CBV Mixins ────────────────────────────────────────────────────────────────

class EmployerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Allows access only to authenticated employers."""
    login_url = reverse_lazy('account:login')

    def test_func(self):
        return self.request.user.role == 'employer'


class EmployeeRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Allows access only to authenticated employees."""
    login_url = reverse_lazy('account:login')

    def test_func(self):
        return self.request.user.role == 'employee'