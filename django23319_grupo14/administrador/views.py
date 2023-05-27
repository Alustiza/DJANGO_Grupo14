from django.shortcuts import render

# Create your views here.
def index_admin(request):
    copyright = 'CaC-Django 2023 - Comisión 23319 - Grupo 14  ©  //  Powered by OpenAI'
    return render(request,'administrador/base.html',{'copyright': copyright})

