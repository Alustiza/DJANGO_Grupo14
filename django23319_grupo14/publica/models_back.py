from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    email = models.EmailField(max_length=150,null=True)
    dni = models.IntegerField(verbose_name="DNI")

class Estudiante(Persona):
    matricula = models.CharField(max_length=10,verbose_name='Matricula')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.matricula} - {self.nombre} {self.apellido}"
    
    # métodos de alta y baja lógica
    def soft_delete(self):
        self.baja=True
        super().save() # save() es un método de models que me permite independizarme del tipo de gestor de bases de datos que estoy usando (es como un insert into)
    
    def restore(self):
        self.baja=False
        super().save()
    
    class Meta():
        verbose_name_plural = 'Estudiantes' # es para que django al expresar el plural no agregue simplemente la s al final del nombre de tabla.
        # db_table = 'nombre_tabla'

class Instructor(Persona):
    legajo = models.CharField(max_length=10,verbose_name='Legajo')

class Categoria(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre

    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()

class Curso(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre') # si quiero hacer PK a este campo, agrego el parámetro primery_key=True 
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio',null=True,default=None)
    portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE) #relacion muchos a uno    

    def __str__(self):
        return self.nombre
    
    def delete(self,using=None,keep_parents=False):
        self.portada.storage.delete(self.portada.name) #borrado fisico
        super().delete()

class Inscripcion(models.Model):
    
    ESTADOS = [
        (1,'Inscripto'),
        (2,'Cursando'),
        (3,'Egresado'),
    ]
    fecha_creacion = models.DateField(auto_now_add=True,verbose_name='Fecha de creacion')
    estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    comision = models.ForeignKey(Comision,on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS,default=1)

    def __str__(self):
        return self.estudiante.nombre
    

    class Perfil(models.Model):
        """MODELO QUE PERMITE DEL USER MODEL DE DJANGO PARA AGREGERLE CAMPOS EXTRAS"""
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        telefono = models.CharField(max_length=20,verbose_name='Teléfono')
        domicilio = models.CharField(max_length=20,verbose_name='Domicilio')
        foto = models.ImageField(upload_to='perfiles/',null=True,verbose_name='Foto Perfil')

class Comision(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    horario = models.CharField(max_length=100,verbose_name="Horario",null=True,default=None)
    link_meet = models.URLField(max_length=100,verbose_name='Link de Meet')
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE) #relacion mucho a uno
    estudiantes = models.ManyToManyField(Estudiante,through='Inscripcion') 

