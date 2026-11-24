from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistroForm, UsuarioForm, PerfilForm
from .models import Perfil


# Registro de usuarios nuevos
def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Se crea el perfil del usuario nuevo
            Perfil.objects.create(user=usuario)
            # Se inicia sesion automaticamente
            login(request, usuario)
            return redirect("perfil")
    else:
        form = RegistroForm()
    return render(request, "accounts/registro.html", {"form": form})


# Muestra el perfil del usuario que inicio sesion
@login_required
def perfil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    return render(request, "accounts/perfil.html", {"perfil": perfil})


# Edita los datos del usuario y su perfil (incluido el avatar)
@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    if request.method == "POST":
        usuario_form = UsuarioForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if usuario_form.is_valid() and perfil_form.is_valid():
            usuario_form.save()
            perfil_form.save()
            return redirect("perfil")
    else:
        usuario_form = UsuarioForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)
    context = {
        "usuario_form": usuario_form,
        "perfil_form": perfil_form,
    }
    return render(request, "accounts/editar_perfil.html", context)