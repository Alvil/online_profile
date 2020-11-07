from django.shortcuts import render
from .forms import UserCredentialsForm
from django.views import generic
from . import models
# Create your views here.


def index(request):
    return render(request, 'index.html')


class UserList(generic.ListView):
    model = models.UserCredentials
    template_name = 'fake/user-list.html'


def create_user(request):
    form = UserCredentialsForm()

    if request.method == 'POST':
        form = UserCredentialsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request, 'createUser.html', {'form': form})
