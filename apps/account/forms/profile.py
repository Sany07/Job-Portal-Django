from django import forms

from account.models import User


class EmployeeProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter Last Name'})

    class Meta:
        model = User
        fields = ["first_name", "last_name", "gender"]

