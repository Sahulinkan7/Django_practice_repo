from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView


class MyRedirectView(RedirectView):
    # url='/'
    pattern_name='home'
    permanent=True