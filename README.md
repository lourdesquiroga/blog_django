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