from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course_django(request):
    return HttpResponse("Hello django course")

def course_python(request):
    return HttpResponse("Hello python course")
