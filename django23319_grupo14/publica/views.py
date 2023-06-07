from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
#from django.conf import settings

from publica.forms import LoginForm
from publica.forms import RegistroForm
from publica.forms import RecuperarForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    mensaje=None
    if(request.method=='POST'):
        login_form = LoginForm(request.POST)
        # acción para tomar los datos del formulario
    else:
        login_form = LoginForm()
    
    context = {                
              'contacto_form':login_form
            }
    
    return render(request,'publica/index.html',context)

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Usuario creado, ya puedes iniciar sesión!')
            return redirect('publica/index.html')
    else:
        form = RegistroForm()
    
    context = {'form': form}

    return render(request,'publica/registrarse.html', context)

# def registrarse(request):
#     mensaje=None
#     if(request.method=='POST'):
#         registro_form = RegistroForm(request.POST)
#         mensaje='Usuario creado, ya puedes iniciar sesión'
#     else:
#         registro_form = RegistroForm()
    
#     copyright = 'CaC-Django 2023 - Comisión 23319 - Grupo 14  ©  //  Powered by OpenAI'

#     context = {                
#                 'mensaje':mensaje,
#                 'registro_form':registro_form,
#                 'copyright':copyright
#             }
    
#     return render(request,'publica/registrarse.html',context)


def home(request):
    mensaje=None

    copyright = 'CaC-Django 2023 - Comisión 23319 - Grupo 14  ©  //  Powered by OpenAI'

    context = {                
                'copyright':copyright,
                'mensaje':mensaje,
            }
    
    return render(request,'publica/home.html',context)

def recuperar(request):
    mensaje=None
    if(request.method=='POST'):
        recuperar_form = RecuperarForm(request.POST)
        mensaje='Contraseña restaurada'
    else:
        recuperar_form = RecuperarForm()
    
    copyright = 'CaC-Django 2023 - Comisión 23319 - Grupo 14  ©  //  Powered by OpenAI'

    context = {                
                'mensaje':mensaje,
                'recuperar_form':recuperar_form,
                'copyright':copyright
            }
    
    return render(request,'publica/forgot_pass.html',context)
