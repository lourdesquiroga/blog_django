from django import forms
from .models import Post


# Formulario basado en el modelo Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "autor", "estado", "imagen"]