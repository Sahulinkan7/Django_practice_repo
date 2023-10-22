from django.shortcuts import render

# Create your views here.
def feesinfo(request):
    info={'cfees':499}
    return render(request,"fees/info.html",info)
