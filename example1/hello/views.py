from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "A/index.html")

def greet(request, name):
    return render(request, "A/greet.html", {"name":name.capitalize()})

def foo(request):
    return HttpResponse("Hello, foo!")