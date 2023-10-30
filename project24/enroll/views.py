from django.shortcuts import render
from .forms import EnrollmentForm

# Create your views here.
def enrollmentview(request):
    if request.method=="POST":
        fm=EnrollmentForm(request.POST)
        if fm.is_valid():
            print("form validated")
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            print(f"{name} {email} {password}")
            fm=EnrollmentForm()
    else:
        fm=EnrollmentForm()
    return render(request,"enroll/enroll.html",{'form':fm})