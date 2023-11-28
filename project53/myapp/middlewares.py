class Mymiddleware:
    def __init__(self,get_response) -> None:
        self.get_response=get_response
        print("One time initialization")
    
    def __call__(self,request):
        print("This is before view")
        response=self.get_response(request)
        print("This is after view ")
        return response
        