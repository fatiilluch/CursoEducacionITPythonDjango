from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Contiene las funciones a donde voy a ir a parar cuando ponga una url
# HttpResponse me genera una pagina web y lo que tome como argumento me lo muestra


def index(request):
    return HttpResponse("Bienvenidos al curso de python")
