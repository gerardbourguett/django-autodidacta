from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hola_mundo(request):
    return HttpResponse("<h1>Hola Mundo</h1>")


def about(request):
    return HttpResponse("<h1>About</h1>")