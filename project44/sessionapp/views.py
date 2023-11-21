from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session['product_id']=23
    request.session['product_price']=999
    request.session['product_brand']='killer'
    return render(request,'setsession.html')


def getsession(request):
    keys=request.session.keys()
    items=request.session.items()
    product_id=request.session['product_id']
    product_price=request.session['product_price']
    return render(request,'getsession.html',{'keys':keys,'items':items,'pid':product_id,'pprice':product_price})
