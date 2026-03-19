from django import forms

from jobapp.models import Applicant, BookmarkJob


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['job']


class JobBookmarkForm(forms.ModelForm):
    class Meta:
        model = BookmarkJob
        fields = ['job']

