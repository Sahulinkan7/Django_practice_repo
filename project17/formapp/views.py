from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def registration(request):
    fm=RegistrationForm()
    return render(request,"formapp/registration.html",{"form":fm})