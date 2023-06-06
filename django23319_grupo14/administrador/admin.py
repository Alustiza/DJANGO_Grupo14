from django.contrib import admin
from administrador.models import  Perfil, Pregunta, Conversacion

# Register your models here.

admin.site.register(Conversacion)

class MateAdminSite(admin.AdminSite):
    site_header = "Administración Mate.AI"
    site_title = "Administración superuser"
    index_title = "Administración del sitio"
    empty_value_display = "No hay datos para mostrar"

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "pregunta", "respuesta", "id_conversacion")
    list_editable = ("pregunta", "respuesta")
    #list_filter = ()
    search_fields = ("pregunta", "respuesta")

class PerfilAdmin(admin.ModelAdmin):
    list_display = ("user", "telefono", "premium")
    #list_filter = ("premium")
    search_fields = ("user", "premium")

# registrar de modelos de admin personalizados

sitio_admin = MateAdminSite(name="mateadmin")
sitio_admin.register(Pregunta, PreguntaAdmin)
sitio_admin.register(Perfil,PerfilAdmin)
