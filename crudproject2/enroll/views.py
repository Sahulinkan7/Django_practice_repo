from typing import Any
from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.base import TemplateView,RedirectView,View
from .forms import MyForm
from .models import Student


class Addshowview(TemplateView):
    template_name='enroll/addshow.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        fm=MyForm()
        students=Student.objects.all()
        context={'form':fm,'students':students}
        return context
    
    def post(self,request):
        fm=MyForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"data saved")
            return HttpResponseRedirect("/")
        
class DeleteView(RedirectView):
    url='/'
    def get_redirect_url(self, *args, **kwargs):
        del_id=kwargs['id']
        Student.objects.get(id=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
    
class Updateview(View):
    def get(self,request,id):
        student=Student.objects.get(id=id)
        fm=MyForm(instance=student)
        return render(request,"enroll/update.html",{'form':fm})
    
    def post(self,request,id):
        student=Student.objects.get(id=id)
        fm=MyForm(request.POST,instance=student)
        if fm.is_valid():
            fm.save()
            messages.success(request,"data updated")
        return render(request,"enroll/update.html",{'form':fm})
            
