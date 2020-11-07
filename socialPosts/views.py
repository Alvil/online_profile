from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


class SocialPostList(SelectRelatedMixin, generic.ListView):
    model = models.SocialPost
    select_related = ('user', 'groups')
    template_name = 'socialPosts/socialPosts_list.html'


class UserPosts(generic.ListView):
    model = models.SocialPost
    template_name = 'socialPosts/socialPosts_user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('user_posts').get(
                username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            # print('test')
            # print(self.post_user.user_posts.all())
            return self.post_user.user_posts.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserPosts, self).get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.SocialPost
    select_related = ('user', 'groups')
    template_name = 'socialPosts/socialPosts_detail.html'

    def get_queryset(self):
        queryset = super(PostDetail, self).get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'groups')
    template_name = 'socialPosts/socialPosts_form.html'
    model = models.SocialPost

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(CreatePost, self).form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.SocialPost
    select_related = ('user', 'groups')
    success_url = reverse_lazy('social_posts:all_post')
    template_name = 'socialPosts/socialPosts_confirm_delete.html'

    def get_queryset(self):
        queryset = super(DeletePost, self).get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super(DeletePost, self).delete(request, *args, **kwargs)