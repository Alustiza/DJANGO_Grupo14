from django.contrib import admin
from publica.models import Perfil, Conversacion, Pregunta


# Register your models here.

admin.site.register(Perfil)

admin.site.register(Conversacion)

admin.site.register(Pregunta)

class MateAdmin(admin.AdminSite):
    site_header = "administración mate.ai"
    site_title = "admin superuser"
    index_title = "admin del sitio mate.ai"
    empty_value_display = "no hay datos para mostrar"

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ("id", "fecha", "pregunta", "respuesta", "id_conversacion_id")
    list_editable = ("pregunta", "respuesta")
    list_filter = ()
    search_fields = ("pregunta", "respuesta")

# registrar de modelos de admin personalizados

sitio_admin = MateAdmin(name="mateadmin")
sitio_admin.register(Pregunta, PreguntaAdmin)
