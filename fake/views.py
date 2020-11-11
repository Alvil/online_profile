from django.shortcuts import render
from .forms import UserCredentialsForm
from django.views import generic
from . import models
# Create your views here.


def home(request):
    return render(request, 'fake/home.html')


class UserList(generic.ListView):
    model = models.UserCredentials
    template_name = 'fake/user-list.html'


def create_user(request):
    form = UserCredentialsForm()

    if request.method == 'POST':
        form = UserCredentialsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)

    return render(request, 'fake/createUser.html', {'form': form})
