from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView, TemplateView


class UserCreate(CreateView):
    form_class = forms.UserCreateForm
    success_url = '/social/accounts/login'
    template_name = 'socialAccounts/signup.html'
