from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

import misaka


User = get_user_model()

from django import template
register = template.Library()


class SocialGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='SocialGroupMembers')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super(SocialGroup, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('social_groups:single_group', kwargs={'slug': self.slug})


class SocialGroupMembers(models.Model):
    group = models.ForeignKey(SocialGroup, related_name='group_members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
