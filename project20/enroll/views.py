from django.shortcuts import render
from .forms import EnrollForm
# Create your views here.
def enrollment(request):
    fm=EnrollForm()
    return render(request,"enroll/registration.html",{'form':fm})