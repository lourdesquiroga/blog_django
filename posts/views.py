from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
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


# READ: muestra todos los posts publicados
def lista_posts(request):
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    context = {
        "posts": posts
    }
    return render(request, "posts/lista_posts.html", context)


# READ: muestra un post completo
def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detalle_post.html", {"post": post})


# CREATE: muestra el formulario vacio y guarda el post nuevo
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect("detalle_post", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "posts/post_form.html", {"form": form, "accion": "Crear post"})


# UPDATE: muestra el formulario con los datos del post y guarda los cambios
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("detalle_post", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "posts/post_form.html", {"form": form, "accion": "Editar post", "post": post})


# DELETE: pide confirmacion y despues borra el post
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("lista_posts")
    return render(request, "posts/post_confirm_delete.html", {"post": post})