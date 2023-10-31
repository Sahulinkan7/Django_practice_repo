from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"user created successfully")
            fm=UserCreationForm()
    else:
        fm=UserCreationForm()
    return render(request,"enroll/signup.html",{"form":fm})
