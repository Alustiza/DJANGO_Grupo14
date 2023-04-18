from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('hola', views.hola, name='hola'),
    path('saludar/<str:nombre>/', views.saludar, name='saludar'),
    path('proyectos/<int:anio>/<int:mes>/', views.ver_proyectos, name='ver_proyectos'),
    path('proyectos/<int:anio>/', views.ver_proyectos_uno, name='ver_proyectos'),

]