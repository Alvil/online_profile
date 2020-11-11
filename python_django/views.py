from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'landing-page.html')


class SocialHomePage(TemplateView):
    template_name = 'social/index.html'
