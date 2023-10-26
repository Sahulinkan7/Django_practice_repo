from django.shortcuts import render

# Create your views here.
def coursepage(request):
    return render(request,"course/courses.html")