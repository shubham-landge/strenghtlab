from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def helloWorld(request):
    msg = 'Hello Shubham'
    return HttpResponse(msg)
