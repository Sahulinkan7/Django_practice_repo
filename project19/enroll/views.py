from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.

def Registration(request):
    fm=RegistrationForm()
    return render(request,"enroll/registration.html",{'form':fm})
