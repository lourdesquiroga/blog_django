from django.shortcuts import render


# Muestra la pagina de inicio
def inicio(request):
    return render(request, "posts/inicio.html")


# Muestra la pagina "Acerca de"
def acerca(request):
    return render(request, "posts/acerca.html")


# Muestra el listado de posts (por ahora con datos escritos en el HTML)
def lista_posts(request):
    return render(request, "posts/lista_posts.html")