from django.shortcuts import render

# Create your views here.
def course_fees(request):
    return render(request,"fees/feesone.html",{'price':499})