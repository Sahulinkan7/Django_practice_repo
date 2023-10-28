from django.shortcuts import render
from .models import Student
# Create your views here.
def studentdetail(request):
    stu=Student.objects.all()
    return render(request,"enroll/studentdetails.html",{'students':stu})