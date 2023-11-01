from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def signup(request):
    if request.method=='POST':
        fm=SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"user creation successfull ! congratulations ")
            fm=SignupForm()
    else:
        fm=SignupForm()
    return render(request,"enroll/enroll.html",{'form':fm})

def login_user(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"user logged in successfully !")
                    return HttpResponseRedirect("/profile/")
        else:
            fm=LoginForm()
        return render(request,"enroll/login.html",{'form':fm})
    else:
        return HttpResponseRedirect("/profile/")

def profile(request):
    if request.user.is_authenticated:
        user=request.user
        return render(request,"enroll/profile.html",{'name':user})
    else:
        return HttpResponseRedirect("/login/")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/login/")