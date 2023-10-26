from django.shortcuts import render

# Create your views here.
def coursespage(request):
    courses=['python','java','javascript','go','django','laravel']
    return render(request,"course/course.html",{'courses':courses})
