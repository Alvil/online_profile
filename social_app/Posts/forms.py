from django import forms

from .models import SocialPost


class NewPost(forms.ModelForm):
    class Meta:
        model = SocialPost
        fields = ('message', 'groups')
