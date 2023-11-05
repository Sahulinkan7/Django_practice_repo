from django.shortcuts import render,HttpResponseRedirect
from .forms import LoginForm,SignupForm,EdituserForm,EditformForAdmin
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
def homelogin(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                usr=authenticate(username=uname,password=upass)
                if usr is not None:
                    login(request,user=usr)
                    return HttpResponseRedirect("/profile/")
        else:
            fm=LoginForm()
        return render(request,"enroll/home.html",{'form':fm})
    else:
        return HttpResponseRedirect("/profile/")

def signupview(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=SignupForm()
        
    return render(request,"enroll/signup.html",{'form':fm})


def logoutuser(request):
    logout(request)
    return HttpResponseRedirect("/")

def profileuser(request,id):
    if request.user.is_superuser:
        iid=User.objects.get(pk=id)
        if request.method=='POST':
            fm=EditformForAdmin(request.POST,instance=iid)
            if fm.is_valid():
                fm.save()
        else:
            fm=EditformForAdmin(instance=iid)
        return render(request,"enroll/profile.html",{'form':fm})
    else:
        id=None
        if request.user.is_authenticated:
            if request.method=='POST':
                fm=EdituserForm(request.POST,instance=request.user)
                if fm.is_valid():
                    fm.save()
            else:
                fm=EdituserForm(instance=request.user)
            return render(request,"enroll/profile.html",{'form':fm})
        else:
            return HttpResponseRedirect("/")
        
def adminpage(request):
    users=User.objects.all()
    return render(request,"enroll/admin.html",{'users':users})