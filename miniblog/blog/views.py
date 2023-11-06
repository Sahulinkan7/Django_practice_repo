from django.shortcuts import render,HttpResponseRedirect
from .forms import BlogForm
from .models import Post
from django.contrib import messages

# Create your views here.
def homeview(request):
    blogs=Post.objects.all()
    return render(request,"blog/home.html",{'blogs':blogs})

def dashboardview(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            blogs=Post.objects.all()
        else:
            blogs=Post.objects.filter(author=request.user.username)
        return render(request,"blog/dashboard.html",{'blogs':blogs})
            
    else:
        return HttpResponseRedirect("/accounts/login/")
    
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            post=Post.objects.get(id=id)
            fm=BlogForm(request.POST,instance=post)
            if fm.is_valid():
                fm.save()
                messages.success(request,"post got updated !")
                return HttpResponseRedirect("/blog/dashboard/")
        else:
            post=Post.objects.get(id=id)
            fm=BlogForm(instance=post)
        return render(request,"blog/updatepost.html",{"form":fm})
    else:
        return HttpResponseRedirect("/accounts/login/")

def deletepost(request,id):
    if request.method=='POST':
        pst=Post.objects.get(pk=id)
        pst.delete()
        messages.success(request,"post deleted successfully !")
        return HttpResponseRedirect("/blog/")
    else:
        return HttpResponseRedirect("/blog/dashboard/")

def writeblogview(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=BlogForm(request.POST)
            if fm.is_valid():
                title=fm.cleaned_data['title']
                desc=fm.cleaned_data['desc']
                author=request.user.username
                Postmodel=Post(title=title,desc=desc,author=author)
                Postmodel.save()
                messages.success(request,"post create successfully !")
                return HttpResponseRedirect("/blog/dashboard/")
        else:
            fm=BlogForm()
        return render(request,"blog/blogpost.html",{'form':fm})
    else:
        return HttpResponseRedirect("/accounts/login/")