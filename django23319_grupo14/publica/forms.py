from django import forms
from django.forms import ValidationError
import re

from administrador.models import Usuario
from django.contrib.auth.forms import UserCreationForm

# class RegistroForm(forms.Form):
#     nombre = forms.CharField(
#         label='Nombre',
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Solo letras'}))
#     apellido = forms.CharField(
#         label='Apellido', 
#         widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Solo letras'}))
#     email = forms.EmailField(
#         label='Email',
#         max_length=50,
#         error_messages={'required': 'Por favor completa el campo'},
#         widget=forms.TextInput(attrs={'class':'form-control','type':'email'}))
#     password = forms.CharField(widget=forms.PasswordInput, label="Password")
#     aceptacion = forms.BooleanField(
#         label='Acepto los términos y condiciones',
#         required=True,
#         widget=forms.CheckboxInput(attrs={'class':'form-check-input','value':1}))

class RegistroForm(UserCreationForm):
    username = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Solo letras'}))
    class Meta:
        model = Usuario
        fields = ['username','email','password1','password2']

class LoginForm(forms.Form):
    
    email = forms.EmailField(label='Email',max_length=50, required=True)
    password = forms.PasswordInput()
    basesycondiciones = forms.BooleanField(
        label='acepto las bases y condiciones',
        required=True
    )

class RecuperarForm(forms.Form):
    
    email = forms.EmailField(label='Email',max_length=50, required=True)

