from django.shortcuts import render,HttpResponseRedirect
from .forms import EnrollmentForm
from .models import Student
# Create your views here.
def home(request):
    if request.method=="POST":
        fm=EnrollmentForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=EnrollmentForm()
    else:
        fm=EnrollmentForm()
    stud=Student.objects.all()[::-1]
    return render(request,"enroll/home.html",{'form':fm,'stu':stud})


def deletedata(request,id):
    if request.method=='POST':
        stu=Student.objects.get(id=id)
        stu.delete()
        return HttpResponseRedirect("/")
    
def editdata(request,id):
    if request.method=="POST":
        obj=Student.objects.get(pk=id)
        fm=EnrollmentForm(request.POST,instance=obj)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        stuobj=Student.objects.get(pk=id)
        fm=EnrollmentForm(instance=stuobj)
    return render(request,"enroll/update.html",{"form":fm,"id":id})