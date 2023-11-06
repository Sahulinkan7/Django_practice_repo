from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import login,logout,update_session_auth_hash,authenticate
from .forms import SignupForm,LoginForm
from django.contrib import messages


# Create your views here.
def signupview(request):
    if request.method=='POST':
        fm=SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"your account created successfully !")
    else:
        fm=SignupForm()
    return render(request,"accounts/signup.html",{'form':fm})

def loginview(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                usr=authenticate(username=uname,password=upass)
                if usr is not None:
                    login(request,user=usr)
                    messages.success(request,"You are logged in successfully ! ")
                    return HttpResponseRedirect("/blog/")
            else:
                messages.error(request,"invalid username or password ! try again ")
                return HttpResponseRedirect("/accounts/login/")
        else:
            fm=LoginForm()
        return render(request,"accounts/login.html",{'form':fm})
    else:
        return HttpResponseRedirect("/blog/dashboard/")

def logoutview(request):
    logout(request)
    messages.success(request,"you are logged out !")
    return HttpResponseRedirect("/accounts/login/")