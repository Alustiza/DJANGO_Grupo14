from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('recuperar', views.recuperar, name='recuperar'),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='publica/index.html',
        extra_context={'variable':'TEST'},
    )),
    path('accounts/', include('django.contrib.auth.urls')),
]