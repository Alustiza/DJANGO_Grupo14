from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('login/', views.MateLoginView.as_view(), name='login'),
    path('logout/', views.MateLogoutView.as_view(), name = 'logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]

