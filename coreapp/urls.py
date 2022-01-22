from django.contrib import admin
from django.urls import path

from .views import helloWorld, contactView

urlpatterns = [
    path('hello/', helloWorld),
    path('contact/', contactView)
]
