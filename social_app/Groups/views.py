from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import SocialGroup, SocialGroupMembers


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    template_name = 'socialGroups/socialGroups_form.html'
    fields = ('name', 'description')
    model = SocialGroup


class SingleGroup(generic.DetailView):
    template_name = 'socialGroups/socialGroups_detail.html'
    model = SocialGroup


class ListGroups(generic.ListView):
    template_name = 'socialGroups/socialGroups_list.html'
    model = SocialGroup


class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('social_groups:single_group', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(SocialGroup, slug=self.kwargs.get('slug'))

        try:
            SocialGroupMembers.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, 'Warning! Already a member!')
        else:
            messages.success(self.request, 'You are now a member!')
        return super(JoinGroup, self).get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('social_groups:single_group', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = SocialGroupMembers.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            )
        except SocialGroupMembers.DoesNotExist:
            messages.warning(self.request, 'Sorry your are not in this group')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group!')

        return super(LeaveGroup, self).get(request, *args, **kwargs)
