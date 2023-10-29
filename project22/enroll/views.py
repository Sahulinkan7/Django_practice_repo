from django.shortcuts import render
from .forms import EnrollForm

# Create your views here.
def enrollment(request):
    if request.method=="POST":
        fm=EnrollForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            print(f" cleaned data : {name} , {email} , {password}")
    else:
        fm=EnrollForm()
    return render(request,"enroll/enroll.html",{'form':fm})
    
