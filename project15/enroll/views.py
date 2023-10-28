from django.shortcuts import render
from .models import Student

# Create your views here.
def students(request):
    stu=Student.objects.all()
    return render(request,"enroll/students.html",{"students":stu})