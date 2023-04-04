from django.shortcuts import render
from django.http import HttpResponse


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


def index(request):
    return render(request,'publica/index.html')


def saludar(request, nombre):
    return HttpResponse({nombre})


def ver_proyectos(request, anio,mes):
    return HttpResponse(f""" Proyectos del {mes} {anio}""")

def ver_proyectos_uno(request, anio,mes=1):
    return HttpResponse(f""" Proyectos del {mes} {anio}""")


def error_404(request, exception):
    return render(request, "404.html")