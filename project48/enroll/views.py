from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Student

class Mylistview(ListView):
    model=Student
    template_name='enroll/students.html'
    context_object_name='students'
    
    # modify the queryset which is being returned as modelname_list or through custom context_object_name
    def get_queryset(self) -> QuerySet[Any]:
        filtereddata=Student.objects.filter(id=2)
        return filtereddata
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        context['allstudents']=Student.objects.all()
        return context