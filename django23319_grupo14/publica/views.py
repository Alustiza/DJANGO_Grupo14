from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.urls import reverse_lazy

from publica.forms import LoginForm, RegistroForm, RecuperarForm

#from django.contrib.auth import authenticate, login, logout

#from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'publica/password_reset.html'
    email_template_name = 'publica/password_reset_email.html'
    subject_template_name = 'publica/password_reset_subject.txt'
    success_message = "Te enviamos un correo electrónico para continuar el proceso de recuperación de contraseña. " \
                      " Si no lo recibiste, verifica el correo electrónico ingresado o la carpeta spam."
    success_url = reverse_lazy('index')

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
            return redirect('index')
    else:
        form = RegistroForm()
    
    context = {'form': form}

    return render(request,'publica/registrarse.html', context)

class MateLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Cuenta o password incorrecto. Intente nuevamente')
        return self.render_to_response(self.get_context_data(form=form))

class MateLogoutView(LogoutView):
    next_page = 'home'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Se ha cerrado la sesión correctamente.')
        return response

@login_required
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
