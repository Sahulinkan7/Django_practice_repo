from django.shortcuts import render

# Create your views here.
def coursepage(request):
    coursedetails={'cname':'Django','ctitle':'Learn Django','cduration':'45 hrs'}
    return render(request,"course/coursepage.html",context=coursedetails)