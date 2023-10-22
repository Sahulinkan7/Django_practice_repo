from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_django(request):
    return HttpResponse("fees of django is 300")

def fees_python(request):
    return HttpResponse('fees of python is 200')