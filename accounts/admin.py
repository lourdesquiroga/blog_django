from django.contrib import admin
from .models import Perfil


# Configura como se ven los perfiles en el panel de administracion
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("user", "link_web")


admin.site.register(Perfil, PerfilAdmin)