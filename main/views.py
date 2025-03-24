from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")

def service(request):
    return render(request, "main/service.html")

def blog(request):
    return render(request, "main/blog.html")

def contact(request):
    return render(request, "main/contact.html")