from typing import Any
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from .models import Student

from django.views.generic.edit import FormView
from .forms import EnrollmentForm

class ContactFormView(FormView):
    template_name='enroll/enroll.html'
    form_class=EnrollmentForm
    success_url='/'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        context['all_students']=Student.objects.all()
        return context 
    
    def form_valid(self, form):
        name=form.cleaned_data['name']
        print(name)
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form) -> HttpResponse:
        return super().form_invalid(form)
    