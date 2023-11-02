from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,LoginForm,PasswordnewForm,Setuserpassword
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.

def signup(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=SignupForm()
    else:
        fm=SignupForm()
    return render(request,"enroll/signup.html",{'form':fm})

def user_login(request):
    if not request.user.is_authenticated: 
        if request.method=='POST':
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                print("form validated")
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                usr=authenticate(username=uname,password=upass)
                if usr is not None:
                    login(request,usr)
                    messages.success(request,"successfully logged in !")
                    return HttpResponseRedirect("/profile/")
        else:
            fm=LoginForm()
        return render(request,"enroll/login.html",{"form":fm})
    else:
        return HttpResponseRedirect("/profile/")

def profile_user(request):
    if request.user.is_authenticated:
        return render(request,"enroll/profile.html",{'name':request.user})
    else:
        return HttpResponseRedirect("/login/")
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/login/")

def passwordchange(request):
    if request.user.is_authenticated: 
        if request.method=='POST':
            fm=PasswordnewForm(user=request.user,data=request.POST)
            if fm.is_valid():
                print("form validate")
                fm.save()
                update_session_auth_hash(request,request.user)
                return HttpResponseRedirect("/profile/")
        else:
            fm=PasswordnewForm(user=request.user)
        return render(request,"enroll/changepassword.html",{'form':fm})
    else:
        return HttpResponseRedirect("/login/")
    
def setnewpassword(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=Setuserpassword(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,request.user)
                return HttpResponseRedirect("/profile/")
        else:
            fm=Setuserpassword(user=request.user)
        return render(request,"enroll/setpassword.html",{"form":fm})
    else:
        return HttpResponseRedirect("/login/")