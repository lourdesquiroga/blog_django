from django.db import models


# Representa una publicacion del blog
class Post(models.Model):
    # Opciones posibles para el estado (valor guardado, texto que se muestra)
    ESTADOS = [
        ("borrador", "Borrador"),
        ("publicado", "Publicado"),
        ("archivado", "Archivado"),
    ]

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="borrador")
    estado = models.CharField(max_length=20, choices=ESTADOS, default="borrador")
    imagen = models.ImageField(upload_to="posts/", null=True, blank=True)

    # Cada post se muestra por su titulo (por ejemplo, en el admin)
    def __str__(self):
        return self.titulo
