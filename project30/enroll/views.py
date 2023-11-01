from django.shortcuts import render
from .forms import SignupForm
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method=='POST':
        fm=SignupForm(request.POST)
        if fm.is_valid():
            print("form validated")
            fm.save()
            messages.success(request,"Congrats you are signed up successfully ! ")
            fm=SignupForm()
    else:
        fm=SignupForm()
    return render(request,"enroll/enroll.html",{"form":fm})