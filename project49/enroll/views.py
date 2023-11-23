from typing import Any
from django.shortcuts import render
from .models import Student
from django.views.generic import ListView,DetailView

class StudentDetailView(DetailView):
    model=Student
    template_name='enroll/student.html' # custom template .. default is appname/model_detail.html
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        context['all_students']=Student.objects.all()
        return context
    
class StudentListView(ListView):
    model=Student
    # context_object_name='students' # default context is modelname_list
