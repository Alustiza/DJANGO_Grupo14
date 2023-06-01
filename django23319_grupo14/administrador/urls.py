from django.urls import path
from . import views


urlpatterns = [

path('administrador/', views.administrador, name='administrador'),
]