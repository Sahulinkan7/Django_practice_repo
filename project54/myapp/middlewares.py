from django.http import HttpResponse

class BrotherMiddleware:
    def __init__(self,get_response) -> None:
        self.get_response=get_response
        print("Brother middleware initialization")
    
    def __call__(self,request):
        print("Brother middlware before view")
        # response= self.get_response(request)
        response= HttpResponse("Bhai se panga nai")
        print("Brother middleware after view")
        return response
    
class FatherMiddleware:
    def __init__(self,get_response) -> None:
        self.get_response=get_response
        print("Father middleware Initialization")
        
    def __call__(self,request):
        print("Father middleware before view")
        response=HttpResponse("Bas ho gaya")
        print("Father middleware after view")
        return response
    
class MotherMiddleware:
    def __init__(self,get_response) -> None:
        self.get_response=get_response
        print("Mother middleware Initialization")
        
    def __call__(self,request):
        print("Mother middleware before view")
        response=self.get_response(request)
        print("Mother middleware after view")
        return response
        