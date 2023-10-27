from django.shortcuts import render

# Create your views here.
def skills(request):
    context={'skills':'active'}
    return render(request,"skills/skills.html",context)