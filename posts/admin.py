from django.contrib import admin
from .models import Post


# Configura como se ven los posts en el panel de administracion
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "estado", "fecha_creacion")


admin.site.register(Post, PostAdmin)