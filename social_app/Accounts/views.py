from django.views.generic import CreateView

from .forms import UserCreateForm


class UserCreate(CreateView):
    form_class = UserCreateForm
    success_url = '/social/accounts/login'
    template_name = 'socialAccounts/signup.html'
