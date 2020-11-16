from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from . import models
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth import get_user_model
from socialPosts.models import SocialPost

User = get_user_model()


class CreateComment(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.SocialComments
    fields = ('comment',)
    template_name = 'socialComments/socialComments_form.html'

    def get_success_url(self):
        return reverse('social_posts:single_post', kwargs={'username': self.object.at_post.user.username,
                                                           'pk': self.object.at_post.pk})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.at_post = SocialPost.objects.get(id=kwargs['pk'])
        self.object.user = self.request.user
        self.object.save()
        return super(CreateComment, self).form_valid(form)


class DeleteComment(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.SocialComments
    select_related = ('user', 'at_post')
    success_url = reverse_lazy('social_posts:single_post')
    template_name = 'socialComments/socialComments_confirm_delete.html'

    def get_queryset(self):
        queryset = super(DeleteComment, self).get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Comment Deleted')
        return super(DeleteComment, self).delete(request, *args, **kwargs)
