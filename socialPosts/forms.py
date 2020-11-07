from . import models
from django import forms


class NewPost(forms.ModelForm):
    class Meta:
        model = models.SocialPost
        fields = ('message', 'groups')
