from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,LoginForm,UserprofileForm,ChangePasswordForm,SetnewpasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages


# Create your views here.
def homelogin(request):
    if request.method=='POST':
        fm=LoginForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            usr=authenticate(username=uname,password=upass)
            if usr is not None:
                login(request,user=usr)
                messages.success(request,"your are logged in successfully !")
                return HttpResponseRedirect("/profile/")
    else:
        fm=LoginForm()
    return render(request,"enroll/login.html",{'form':fm})

def signup(request):
    if request.method=='POST':
        fm=SignupForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['username']
            fm.save()
            fm=SignupForm()
            messages.success(request,f" dear {name} , your acount created successfully. please login !")
            return HttpResponseRedirect("/")
    else:
        fm=SignupForm()
    return render(request,"enroll/signup.html",{'form':fm})

def changepass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=ChangePasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()

        else:
            fm=ChangePasswordForm(user=request.user)
        return render(request,"enroll/passwordchange.html",{'form':fm})

def setnewpass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=SetnewpasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,request.user)
                return HttpResponseRedirect("/profile/")
        else:
            fm=SetnewpasswordForm(user=request.user)
        return render(request,"enroll/setnewpassword.html",{'form':fm})
    else:
        return HttpResponseRedirect("/")

def logout_user(request):
    logout(request)
    messages.success(request,"You are logged out successfully !")
    return HttpResponseRedirect('/')

def user_profile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=UserprofileForm(request.POST,instance=request.user)
            if fm.is_valid():
                name=fm.cleaned_data['username']
                fm.save()
                messages.success(request,f"dear {name} , your profile updated. ")
        else:
            fm=UserprofileForm(instance=request.user)
        return render(request,"enroll/profile.html",{'form':fm})
    else:
        return HttpResponseRedirect("/")

