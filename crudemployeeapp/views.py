from django.http import HttpResponse,JsonResponse

# def aboutus(request):
#     return HttpResponse("Welcome to django")
# def employee(request):
#     return HttpResponse("Welcome to employee")
# def home(request):
#     return HttpResponse("Welcome to home")
# def employeedata(request,employeeid):
#     return HttpResponse(employeeid)

# ???????????????????????????



def home_page(request):
    print("home page request")
    friend=[
        'aniket',
        'abhishek',
        'ajay'
    ]
    return JsonResponse(friend,safe=False)
