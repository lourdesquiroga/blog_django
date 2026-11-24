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