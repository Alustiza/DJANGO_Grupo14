from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola mundo Django!!!!")



def index(request):
    return HttpResponse("nada funciona")
