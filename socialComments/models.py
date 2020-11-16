from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from socialPosts.models import SocialPost
import misaka

User = get_user_model()


class SocialComments(models.Model):
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.DO_NOTHING)
    at_post = models.ForeignKey(SocialPost, related_name='post_comments', null=True, on_delete=models.CASCADE)
    comment = models.TextField(max_length=256)
    comment_html = models.TextField(editable=False)
    commented_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    def save(self, *args, **kwargs):
        self.comment_html = misaka.html(self.comment)
        super(SocialComments, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-commented_at']
