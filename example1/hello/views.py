from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def greet(reqyest, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def foo(request):
    return HttpResponse("Hello, foo!")