from braces.views import SelectRelatedMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic

from .models import SocialComments
from social_app.Posts.models import SocialPost

User = get_user_model()


class CreateComment(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = SocialComments
    fields = ('comment',)
    template_name = 'socialComments/socialComments_form.html'

    def get_success_url(self):
        return reverse('social_posts:single_post', kwargs={'username': self.object.at_post.user.username,
                                                           'pk': self.object.at_post.pk})

    def post(self, request, *args, **kwargs):
        # need to override post method since it needs to accept kwargs
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


# feature still not implemented
# class DeleteComment(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
#     model = SocialComments
#     select_related = ('user', 'at_post')
#     # success_url = reverse_lazy('social_posts:single_post')
#     template_name = 'socialComments/socialComments_confirm_delete.html'
#
#     def get_queryset(self):
#         queryset = super(DeleteComment, self).get_queryset()
#         return queryset.filter(user_id=self.request.user.id)
#
#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request, 'Comment Deleted')
#         self.object = self.get_object()
#         return super(DeleteComment, self).delete(request, *args, **kwargs)
#
#     def get_success_url(self, **kwargs):
#         return reverse_lazy('social_posts:single_post', kwargs={'pk': self.object.at_post.pk,
#                                                                 'username': self.object.at_post.user.username})
