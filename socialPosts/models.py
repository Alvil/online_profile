from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka
from socialGroups.models import SocialGroup
from django.contrib.auth import get_user_model

User = get_user_model()


class SocialPost(models.Model):
    user = models.ForeignKey(User, related_name='user_posts', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256, default='---')
    title_html = models.CharField(max_length=256, editable=False, default='---')
    message = models.TextField()
    message_html = models.TextField(editable=False)
    groups = models.ForeignKey(SocialGroup, related_name='group_posts', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        self.title_html = misaka.html(self.title)
        super(SocialPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('social_posts:single_post', kwargs={'username': self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']













