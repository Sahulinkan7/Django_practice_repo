from django.shortcuts import render

# Create your views here.
def fees_dj(request):
    return render(request,"feesone.html")

def fees_py(request):
    return render(request,"feestwo.html")