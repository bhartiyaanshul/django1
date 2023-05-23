from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("This is About Page")
def service(request):
    return HttpResponse("This is Service Page")
def contact(request):
    return HttpResponse("This is Contact Page")

