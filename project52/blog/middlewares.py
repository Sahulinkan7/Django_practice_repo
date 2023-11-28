from django.http import HttpResponse

def myfirstmiddleware(get_response):
    print('Initial run custom middleware 1')
    def my_function(request):
        print("This is first middleware before view")
        response= get_response(request)
        print("This is first middleware after view")
        return response
    return my_function


def mysecondmiddleware(get_response):
    print('Initial run custom middleware 2')
    def my_function(request):
        print("This is second middleware before view")
        response= get_response(request)
        print("This is second middleware after view")
        return response
    return my_function

# def mysecondmiddleware(get_response):
#     print('Initial run custom middleware 2')
#     def my_function(request):
#         print("This is second middleware before view")
#         if request.user.is_authenticated:
#             response= get_response(request)
#         else:
#             response= HttpResponse("NIKAL")
#         print("This is second middleware after view")
#         return response
#     return my_function