from django.shortcuts import render

# Create your views here.
def set_cookie(request):
    response = render(request,"index.html")
    response.set_cookie('name','linkan',max_age=60*60*24)
    return response
    
def get_cookie(request):
    name=request.COOKIES.get('name')
    return render(request,"getcookie.html",{'name':name})