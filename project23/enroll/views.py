from django.shortcuts import render
from .forms import EnrollmentForm
# Create your views here.
def enroll(request):
    if request.method=="POST":
        fm=EnrollmentForm(request.POST)
        if fm.is_valid():
            print("form is validated")
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            print(f"name : {name} , email : {email} , password : {password}")
            fm=EnrollmentForm()
    else:
        fm=EnrollmentForm()
    return render(request,"enroll/enroll.html",{'form':fm})