from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def helloWorld(request):
    msg = 'Hello Shubham'
    return HttpResponse(msg)


def contactView(request):
    contact = 'Manoj K, 7588426773, subhamlandge007@gmail.com'
    return HttpResponse(contact)

