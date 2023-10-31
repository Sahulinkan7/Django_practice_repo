from django.shortcuts import render

# Create your views here.
def home(request,myid,subid=0):
    return render(request,"enroll/home.html",{'id':myid,'id2':subid})