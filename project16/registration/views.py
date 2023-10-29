from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def registration(request):
    fm=StudentRegistration(auto_id=True,label_suffix=' -- ',initial={'name':'Linkan'})
    fm.order_fields(field_order=['school_name','email','name'])
    return render(request,"registration/registration.html",{"form":fm})
