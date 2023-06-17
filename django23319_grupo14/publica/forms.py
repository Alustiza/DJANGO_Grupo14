from django import forms
from administrador.models import Usuario
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirme contraseña'

    class Meta:
        model = Usuario
        fields = ['username','email','password1','password2']
        labels = {'username': 'Nombre de usuario', 'email': 'Correo electrónico'}
        error_messages={
           "username": {"required": "Este campo es obligatorio"},
           "email": {"required": "Este campo es obligatorio"},
       }

class LoginForm(forms.Form):
    
    email = forms.EmailField(label='Email',max_length=50, required=True)
    password = forms.PasswordInput()
    basesycondiciones = forms.BooleanField(
        label='acepto las bases y condiciones',
        required=True
    )

class RecuperarForm(forms.Form):
    
    email = forms.EmailField(label='Email',max_length=50, required=True)

