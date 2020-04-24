from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from account.models import User


class EmployeeRegistrationForm(UserCreationForm):

    class Meta:

        model=User

        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'gender']
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'gender': {
                'required': 'Gender is required'
            }
        }
    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        user.role = "employee"
        if commit:
            user.save()
        return user


class EmployerRegistrationForm(UserCreationForm):

    class Meta:

        model=User

        fields = ['first_name', 'last_name', 'email', 'password1', 'password2',]


    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        user.role = "employer"
        if commit:
            user.save()
        return user

