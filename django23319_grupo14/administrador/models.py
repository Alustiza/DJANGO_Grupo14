from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    pass

class Perfil(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    telefono = models.CharField(max_length=20,verbose_name='Teléfono')
    premium = models.BooleanField(default=1)
    foto = models.ImageField(upload_to='perfiles/',null=True,verbose_name='Foto Perfil')

    def __str__(self):
        return f"{self.user} - {self.telefono} - {self.premium} {self.foto}"
    

    class Meta():
        verbose_name_plural = "Perfiles"

class Conversacion(models.Model):
    fecha = models.DateField(verbose_name='Fecha de conversacion',null=True,default=None)
    id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE) #relacion muchos a uno 

    def __str__(self):
        return f"{self.conversacion}"
    
    class Meta():
        verbose_name_plural = "Conversaciones"


class Pregunta(models.Model):
    fecha = models.DateField(verbose_name='Fecha de pregunta',null=True,default=None)
    pregunta = models.CharField(max_length=300,verbose_name='pregunta')
    respuesta = models.CharField(max_length=300,verbose_name='respuesta')
    id_conversacion = models.ForeignKey(Conversacion,on_delete=models.CASCADE) #relacion muchos a uno 

    def __str__(self):
        return f"{self.fecha} - {self.id_conversacion} - {self.pregunta} {self.respuesta}"
    
    class Meta():
        verbose_name_plural = "Preguntas"