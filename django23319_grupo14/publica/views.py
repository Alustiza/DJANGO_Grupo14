from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola mundo Django!!!!")



# def index(request):
#     if(request.method=="GET"):
#         titulo ="título cuando accedo por get"
#     else:
#         titulo = "título por otros métodos"
    
#     parametro_uno = request.GET.get("param")
#     parametro_dos = request.GET.get("param2")
    
#     return HttpResponse(f"""proyecto Django {titulo} --- {parametro_uno} ---- {parametro_dos}""")

# Para probarlo:
# http://127.0.0.1:8000/?param=2024&param2=hola20202


# def index(request):
#     return render(request,'publica/index.html')


# si quiero enviar un param por el navegador escribo en la url
# http://127.0.0.1:8000/?param=lalaloopp&param2=lolo


def index(request):
    
    copyright = 'TEST - Grupo 14 - Comisión 23319 © 2023 /// powered by OpenAI'

    context = {'copyright':copyright}
    
    return render(request,'publica/index.html',context)



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


def saludar(request, nombre):
    return HttpResponse({nombre})


def ver_proyectos(request, anio,mes):
    return HttpResponse(f""" Proyectos del {mes} {anio}""")

def ver_proyectos_uno(request, anio,mes=1):
    return HttpResponse(f""" Proyectos del {mes} {anio}""")


def error_404(request, exception):
    return render(request, "404.html")