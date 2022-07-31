Cliente --> Servidor

JSON = JavaScript object notation

Direccion IP o un dominio (URL)
HTTP = protocolo hypertext transfer protocole
S = secure

a traves del protocolo, nosotros como clientes, hacemos una peticion(request), y el servidor nos envia una respuesta (response)

indicador de que operacion quiero ejecutar en la URL:
GET
POST

GET es cuando yo quiero, desde el server, obtener datos. No modificar ni grabar nada, solo obtener.
POST es cuando yo quiero grabar, modificar y eliminar datos. Realia movimientos importantes en una BD.

GET y POST son los que se usan en Django. --> no vamos a usar PUT y DELETE

Arquitectura REST = acceder a recursos de una pagina.

www.paginaWeb.com/nombrerecurso 

Protocolo GCI (Common Gateway Interface): antes de REST

para trabajar con un recurso se utilizaba un archivo generado por un lenguaje (ej php)

tenia que acceder a un archivo desde la url y ese archivo me representaba todo el contenido. 

Ej: www.universidadnn.com/alumnos.php

aparecen los frameworks y se deja de utilizar este protocolo y se empeza a usar el protocolo
WSGI (Web Server Gateway Interface) --> no accedemos a a un archivo ejecutable directamente al buscar un recurso,
sino que accedemos a funciones y con ellas podiamos buscar datos en una bse de datos.

otros frameworks de python:
- web2py
- pyramid
- bottle
- flask
- fastApi

las funciones toman como argumento un request (diccionario con el tipo de request) y lo devolvemos a traves de un response

crear el esquema para un proyecto

django-admin startproject <nombre del proyecto>

cuando abrimos el proyecto aparecenuna carpeta: 
libreria con la config inicial de mi proyecto
    tiene un conjunto de modulos
    init.py: indica q estamos dentro de una libreria
    asgi: no se utiliza
    settings.py: esta toda la config del proyecto
manage.py: se utiliza de forma interna para crear nuevas apps, genera las migraciones de las tablas en las bases de datos. 

settings.py:
INSTALLED_APPS: variable que contiene una lista con las distintas aplicaciones que va a tener mi proyecto

DATABASES:diccionario con las conf de las BD

STATIC_URL: ruta donde van a estar los archivos estaticos. Son aquellos archivos que no modifican nada, por ejemplo las imagenes, archivos css, archivos de JavaScript 

Servidor a modo de pruebas: python3 manage.py runserver  

Crear una aplicacion: python3 manage.py startapp nombreApp 
    me crea una carpeta con modulos (libreria).
    al tener el __init__.py django ya sabe que esa app va a ser una libreria 

para que el proyecto conozca la aplicacion, la tengo que agregar en INSTALLED_APPS

urls.py hay que agregarlo manualmente porque django no lo agrega
- sirve para manejar las url's dentro de la aplicacion
- dentro de este modulo (prjClase.urls) van a estar las direcciones que cuando uno las escriba en el navegador, nos van a apuntar a las funciones

dentro de proyecto.urls: 
cada path que definimos va a apuntar a cada app que tengamos

