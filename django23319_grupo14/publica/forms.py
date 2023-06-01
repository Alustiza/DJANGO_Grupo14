from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Solo letras'}))
    apellido = forms.CharField(
        label='Apellido', 
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Solo letras'}))
    email = forms.EmailField(
        label='Email',
        max_length=50,
        error_messages={'required': 'Por favor completa el campo'},
        widget=forms.TextInput(attrs={'class':'form-control','type':'email'}))
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    aceptacion = forms.BooleanField(
        label='Acepto los términos y condiciones',
        required=True,
        widget=forms.CheckboxInput(attrs={'class':'form-check-input','value':1}))


class LoginForm(forms.Form):
    
    email = forms.EmailField(label='Email',max_length=50, required=True)
    password = forms.PasswordInput()
    basesycondiciones = forms.BooleanField(
        label='acepto las bases y condiciones',
        required=True
    )

class RecuperarForm(forms.Form):
    
    email = forms.EmailField(label='Email',max_length=50, required=True)



class ContactoForm(forms.Form):
    TIPO_CONSULTA = (
        ('','-Seleccione-'),
        (1,'Inscripciones'),
        (2,'Soporte del Aula Virtual'),
        (3,'Ser docente'),
    )

    nombre = forms.CharField(label='Nombre y Apellido',required=False)
    email = forms.EmailField(label='Email',max_length=50)
    asunto = forms.CharField(label='Asunto')
    mensaje = forms.CharField(label='Mensaje')
    tipo_consulta = forms.ChoiceField(
        label='Tipo de consulta',
        choices=TIPO_CONSULTA,
        initial=2
    )
    suscripcion = forms.BooleanField(
        label='Deseo suscribirme a las novedades',
        required=False
    )