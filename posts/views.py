from django.shortcuts import render
from .models import Post


# Muestra la pagina de inicio con los ultimos posts publicados
def inicio(request):
    ultimos_posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")[:3]
    context = {
        "ultimos_posts": ultimos_posts
    }
    return render(request, "posts/inicio.html", context)


# Muestra la pagina "Acerca de"
def acerca(request):
    return render(request, "posts/acerca.html")


# Muestra todos los posts publicados, del mas nuevo al mas viejo
def lista_posts(request):
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    context = {
        "posts": posts
    }
    return render(request, "posts/lista_posts.html", context)