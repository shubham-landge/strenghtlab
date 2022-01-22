from django.contrib import admin
from django.urls import path

from .views import helloWorld

urlpatterns = [
    path('hello/', helloWorld),
]
