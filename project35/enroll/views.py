from django.shortcuts import render,HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import Student
from django.contrib import messages


# Create your views here.
def homelogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
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
    
def profileview(request):
    students=Student.objects.all()
    return render(request,"enroll/profile.html",{'students':students})

def deletedata(request,id):
    st=Student.objects.get(id=id)
    if request.user.has_perm('enroll.delete_student'):
        st.delete()
        messages.success(request,"deleted data successfully !")
    else:
        print("no permission to delete")
        messages.error(request,"you do not have permission to delete ")
    return HttpResponseRedirect("/profile/")

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect("/")