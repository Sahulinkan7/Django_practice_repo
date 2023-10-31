from django.shortcuts import render
from .forms import EnrollForm
from django.contrib import messages

# Create your views here.
def enrollview(request):
    if request.method=='POST':
        fm=EnrollForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=EnrollForm()
            messages.success(request,"data saved successfully !")
            messages.warning(request,"data saved successfully !")
            messages.error(request,"data saved successfully !")
            messages.info(request,"data saved successfully !")
    else:
        fm=EnrollForm()
    return render(request,"enroll/enroll.html",{'form':fm})