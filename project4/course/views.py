from django.shortcuts import render

# Create your views here.
def courselist(request):
    students={'stud1':{'name':'rahul','roll':101},
              'stud2':{'name':'linkan','roll':102},
              'stud3':{'name':'lipan','roll':103},
              'stud4':{'name':'subham','roll':104},}
    students={'students':students}
    return render(request,"course/courseone.html",students)