from django import forms
from .models import UserCredentials


class UserCredentialsForm(forms.ModelForm):
    class Meta:
        model = UserCredentials
        fields = '__all__'

