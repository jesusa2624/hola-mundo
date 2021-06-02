from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones(metodos)
# MVT = Modelo Vista Template -> Acciones(metodos)

def hola_mundo(request):
    return HttpResponse ("Hola mundo con Django!!")

