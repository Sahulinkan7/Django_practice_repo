from django.shortcuts import render

# Create your views here.
def fees_django(request):
    fees={'price':'999'}
    return render(request,"fees/feesone.html",context=fees)

def fees_python(request):
    fees={'price':'699'}
    return render(request,"fees/feestwo.html",context=fees)