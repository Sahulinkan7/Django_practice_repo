from django.shortcuts import render
from .models import Students
from datetime import date
from django.db.models import Avg,Count,Sum
# Create your views here.
def home(request):
    # students_data=Students.objects.all()
    # students_data=Students.objects.filter(marks__gte=88)
    # students_data=Students.objects.filter(marks__lte=80)
    # students_data=Students.objects.filter(city__startswith='J')
    # students_data=Students.objects.filter(city__contains='o')
    # students_data=Students.objects.filter(name__contains='L')
    # students_data=Students.objects.filter(name__exact='Linkan')
    # students_data=Students.objects.filter(email__contains='tcs')
    # students_data=Students.objects.filter(admdatetime__year=2021)
    # students_data=Students.objects.filter(passdatetime__month=6)
    # students_data=Students.objects.filter(admdatetime__date=date(2021,11,3))
    students_data=Students.objects.filter(passdatetime__range=(date(2023,11,1),date(2023,12,1)))
    avgmarks=Students.objects.all().aggregate(Avg('marks'))
    totalmarks=Students.objects.all().aggregate(Sum('marks'))
    return render(request,"school/index.html",{'students':students_data,'average':avgmarks,'total':totalmarks})