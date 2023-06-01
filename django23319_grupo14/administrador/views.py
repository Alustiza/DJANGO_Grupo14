from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def administrador(request):
    return render(request,'administrador/index.html')