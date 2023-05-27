from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from publica.forms import LoginForm
from publica.forms import ContactoForm
from publica.forms import RegistroForm
from publica.forms import RecuperarForm

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
    mensaje=None
    if(request.method=='POST'):
        registro_form = RegistroForm(request.POST)
        mensaje='Usuario creado, ya puedes iniciar sesión'
    else:
        registro_form = RegistroForm()
    
    copyright = 'CaC-Django 2023 - Comisión 23319 - Grupo 14  ©  //  Powered by OpenAI'

    context = {                
                'mensaje':mensaje,
                'registro_form':registro_form,
                'copyright':copyright
            }
    
    return render(request,'publica/registrarse.html',context)


def home(request):
    mensaje=None
    if(request.method=='POST'):
        contacto_form = ContactoForm(request.POST)
        mensaje='Hemos recibido tus datos'
        # acción para tomar los datos del formulario
    else:
        contacto_form = ContactoForm()
    
    copyright = 'CaC-Django 2023 - Comisión 23319 - Grupo 14  ©  //  Powered by OpenAI'

    context = {                
                'copyright':copyright,
                'mensaje':mensaje,
                'contacto_form':contacto_form
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




















""" 

def hola(request):
    
    copyright = 'prueba'

    context = {'copyright2':copyright}
    
    return render(request,'publica/hola_openai.html',context)
 """

""" def index(request):
    if(request.method=='GET'):
        titulo = 'Titulo cuando accedo por GET'
    else:
        titulo = 'Titulo cuando accedo por otro metodo'
    parametro_uno = request.GET.get('param')
    parametro_dos = request.GET.get('param2')
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programación',
        },
        {
            'nombre':'Diseño UX/UI',
            'descripcion':'🖌🎨',
            'categoria':'Diseño',
        },
        {
            'nombre':'Big Data',
            'descripcion':'test',
            'categoria':'Análisis de Datos',
        },
        {
            'nombre':'Habilidades blandas',
            'descripcion':'accenture',
            'categoria':'Análisis de Datos',
        },
    ]

    context = {'titulo':titulo,
                'parametro_uno':parametro_uno,
                'hoy':datetime.now(),
                'cursos':listado_cursos
            }
    
    return render(request,'publica/index.html',context) """


# def saludar(request, nombre):
#     return HttpResponse({nombre})


# def ver_proyectos(request, anio,mes):
#     return HttpResponse(f""" Proyectos del {mes} {anio}""")

# def ver_proyectos_uno(request, anio,mes=1):
#     return HttpResponse(f""" Proyectos del {mes} {anio}""")


# def error_404(request, exception):
#     return render(request, "404.html")