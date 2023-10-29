from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EnrollmentForm

# Create your views here.
def success(request):
    return render(request,"enroll/success.html")

def enrolluser(request):
    if request.method=="POST":
        fm=EnrollmentForm(request.POST)
        if fm.is_valid():
            print("form validated")
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            print(f"The cleaned data ---- name : {name} , email: {email} , password: {password}")
            return HttpResponseRedirect("/enroll/success")
    else:
        fm=EnrollmentForm()
    return render(request,"enroll/enroll.html",{'form':fm})