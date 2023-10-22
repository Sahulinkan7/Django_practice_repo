from django.shortcuts import render

# Create your views here.
def learn_django(request):
    coursedetail={"cname":"Django","cduration":"4 months"}
    return render(request,"courses/courseone.html",context=coursedetail)

def learn_python(request):
    coursedetail={"cname":"Python","cduration":"2 months"}
    return render(request,"courses/coursetwo.html",context=coursedetail)