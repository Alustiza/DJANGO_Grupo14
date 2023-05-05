from django import forms

class RegistroForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    email = forms.EmailField(label='Email',max_length=50)
    password = forms.PasswordInput()
    fecha_nacimiento = forms.DateInput()


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


class LoginForm(forms.Form):
    
    email = forms.EmailField(label='Email',max_length=50, required=True)
    password = forms.PasswordInput()
    basesycondiciones = forms.BooleanField(
        label='acepto las bases y condiciones',
        required=True
    )