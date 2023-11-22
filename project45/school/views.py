from django.shortcuts import render,HttpResponse
from django.views import View
from .forms import MyForm
# Create your views here.
def funhome(request):
    return render(request,"school/homefun.html")

class Homeclassview(View):
    def get(self,request):
        return render(request,"school/homeclass.html")
    
class Homecontactview(View):
    def get(self,request):
        fm=MyForm()
        return render(request,"school/forms.html",{'form':fm})
    
    def post(self,request):
        fm=MyForm(request.POST)
        if fm.is_valid():
            print("form is valid")
        return HttpResponse("Your form submitted !")
    

######################################################################################

# passing context to class view 

class Home2View(View):
    info="Hi hello Namaskar"
    def get(self,request):
        return render(request,"school/contextdata.html",{'data':self.info})
    
# passing different template files to single view

class Home3View(View):
    info="Hi hello namaskar"
    template_name=''
    def get(self,request):
        return render(request,self.template_name,{'data':self.info})