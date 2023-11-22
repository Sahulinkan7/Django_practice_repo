from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomeTemplateView(TemplateView):
    template_name='school/home.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['name']='Linkan kumar sahu'
        context['class']=12
        # context={'name':'lipan','email':'sahulinkan7@gmail.com'} # it will be returned by ignoring above context and extra context data
        print(kwargs) # it will print kwargs coming from url
        return context
