from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
    

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    telefono = models.CharField(max_length=20,verbose_name='Teléfono', blank=True)
    premium = models.BooleanField(default=False)
    
    foto = models.ImageField(upload_to='static/perfiles/',null=True,verbose_name='Foto Perfil')

    def __str__(self):
        return f"{self.user} - {self.telefono} - {self.premium} {self.foto}"
  
    class Meta():
        verbose_name_plural = "Perfiles"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)