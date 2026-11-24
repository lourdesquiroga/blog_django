# Blog Django

Proyecto base de un blog web desarrollado con Django.

## Descripción

Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog. Incluye la configuración base del proyecto (blog_project) y una aplicación llamada posts.

## Instalación

Clonar el repositorio:

    git clone https://github.com/lourdesquiroga/blog_django.git

Entrar a la carpeta del proyecto:

    cd blog_django

Crear el entorno virtual:

    python -m venv venv

Activar el entorno virtual.

En Windows PowerShell:

    .\venv\Scripts\Activate.ps1

En Linux o macOS:

    source venv/bin/activate

Instalar las dependencias:

    pip install -r requirements.txt

## Ejecutar el servidor

    python manage.py runserver

Abrir en el navegador: http://127.0.0.1:8000/

## Aplicaciones

## Páginas del sitio

Con el servidor funcionando, se puede entrar a:

- Inicio: http://127.0.0.1:8000/
- Posts: http://127.0.0.1:8000/posts/
- Acerca de: http://127.0.0.1:8000/acerca/

## Estructura de templates y estáticos

- posts/templates/posts/base.html: plantilla base con el menú, de la que heredan las demás páginas.
- posts/templates/posts/inicio.html, acerca.html y lista_posts.html: páginas del sitio.
- posts/static/posts/css/estilos.css: estilos del sitio.

## Base de datos y panel de administración

El proyecto usa SQLite. La base de datos (db.sqlite3) no se sube al repositorio, así que hay que crearla aplicando las migraciones:

    python manage.py migrate

Crear un usuario administrador:

    python manage.py createsuperuser

Levantar el servidor y entrar al panel:

    http://127.0.0.1:8000/admin/

Desde el panel se pueden crear, editar y borrar posts. En la página de Posts solo se muestran los que tienen estado "Publicado".

## Modelo Post

El modelo Post (posts/models.py) tiene los campos titulo, contenido, autor, fecha_creacion (se completa automáticamente) y estado (borrador, publicado o archivado).

## CRUD de posts

Desde el sitio se pueden gestionar los posts sin entrar al admin:

- Listar: http://127.0.0.1:8000/posts/ (muestra los posts publicados)
- Ver detalle: tocando el título de un post (posts/<id>/)
- Crear: link "Nuevo post" del menú (posts/crear/)
- Editar: botón "Editar" en el detalle (posts/<id>/editar/)
- Eliminar: botón "Eliminar" en el detalle, con una página de confirmación antes de borrar (posts/<id>/eliminar/)

El formulario está hecho con un ModelForm (PostForm, en posts/forms.py).

## Imágenes

Cada post puede tener una imagen opcional (campo imagen, un ImageField del modelo Post).

Dependencia nueva: Pillow, necesaria para usar ImageField. Ya está incluida en requirements.txt.

Configuración:

- En settings.py se definieron MEDIA_URL = "/media/" y MEDIA_ROOT = BASE_DIR / "media". Las imágenes se guardan en la carpeta media/posts/.
- En blog_project/urls.py se agregó la configuración para que Django muestre las imágenes durante el desarrollo.
- El formulario usa enctype="multipart/form-data" y las views de crear y editar reciben request.FILES.
- La carpeta media/ está en el .gitignore, porque las imágenes subidas son datos locales.

Cómo probar la carga de imágenes:

1. Aplicar las migraciones con python manage.py migrate.
2. Levantar el servidor con python manage.py runserver.
3. Entrar a "Nuevo post", completar los datos, elegir una imagen y guardar.
4. La imagen se ve en el detalle del post y en el listado.

## Usuarios y perfiles

El proyecto tiene una app llamada accounts para todo lo relacionado con usuarios. Usa el sistema de autenticación de Django (django.contrib.auth).

Antes de usarlo hay que aplicar las migraciones, porque se agregó el modelo Perfil:

    python manage.py makemigrations
    python manage.py migrate

### Registro

Desde "Registrarse" (http://127.0.0.1:8000/accounts/registro/) se crea un usuario nuevo con un formulario basado en UserCreationForm. Al registrarse se crea automáticamente su perfil (Perfil.objects.create en la vista de registro) y queda con la sesión iniciada.

### Iniciar y cerrar sesión

- Iniciar sesión: http://127.0.0.1:8000/accounts/login/ (usa LoginView de Django).
- Cerrar sesión: botón "Cerrar sesión" del menú (usa LogoutView). Después de cerrar sesión se vuelve al listado de posts.

El menú cambia según el usuario: si no inició sesión muestra "Iniciar sesión" y "Registrarse"; si inició sesión muestra "Crear post", "Mi perfil", "Cerrar sesión" y un saludo.

### Modelo Perfil

El modelo Perfil (accounts/models.py) está relacionado con User mediante un OneToOneField, así cada usuario tiene un único perfil. Tiene los campos biografia, link_web y avatar. Está registrado en el panel de administración.

### Avatares

El avatar es un ImageField que guarda las imágenes en media/avatares/. Usa la misma configuración de MEDIA_URL y MEDIA_ROOT que las imágenes de los posts. La vista de editar perfil recibe request.FILES para poder subir la imagen.

- Ver perfil: http://127.0.0.1:8000/accounts/perfil/
- Editar perfil (biografía, link, avatar, nombre, apellido y email): http://127.0.0.1:8000/accounts/perfil/editar/

### Rutas protegidas

Estas vistas requieren haber iniciado sesión (usan @login_required). Si se entra sin sesión, se redirige al login:

- Crear post: posts/crear/ (también post/nuevo/)
- Editar post: posts/<id>/editar/
- Eliminar post: posts/<id>/eliminar/
- Ver y editar el perfil: accounts/perfil/ y accounts/perfil/editar/

El listado y el detalle de los posts siguen siendo públicos.