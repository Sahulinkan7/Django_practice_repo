from django.shortcuts import render
from .forms import EnrollmentForm
from .models import StudentModel
# Create your views here.
def enrollview(request):
    if request.method=='POST':
        fm=EnrollmentForm(request.POST)
        if fm.is_valid():
            print("form validated ")
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            obj=StudentModel(name=name,email=email,password=password)
            obj.save()
            # fm.save()
            fm=EnrollmentForm()
    else:
        fm=EnrollmentForm()
    return render(request,"enroll/enroll.html",{'form':fm})