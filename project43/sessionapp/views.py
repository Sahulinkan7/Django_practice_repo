from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['fname']='lipan'
    request.session['lname']='sahu'
    return render(request,"setsession.html")

def getsession(request):
    fname=request.session['fname']
    lname=request.session['lname']
    return render(request,"getsession.html",{'fname':fname,'lname':lname})