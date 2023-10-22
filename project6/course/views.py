from django.shortcuts import render

# Create your views here.
def coursepage(request):
    course={'course':'Django','duration':'48 hrs'}
    return render(request,"course/info.html",{'course':course})