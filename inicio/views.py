from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Celular
import random
from inicio.forms import CrearCelularFormulario
def inicio(request):
     return HttpResponse ("Bienvenidos a la tienda de celulares")
    
def crear_celulares (request, marca, modelo):
    celular = celular (marca= marca, modelo = modelo)
    celular.save ()
    return render(request,"celulares.html", {"celualr": celular})

def crear_Celular_2 (request):
    
    print ("valor de la request; ", request)
    print ("valor de GET; ", request.GET)
    print ("valor de POST; ", request.POST)
    
    formulario = CrearCelularFormulario()
    
    if request.method == "POST":
      formulario = CrearCelularFormulario(request.POST)
      if formulario.is_valid ():
       datos = formulario.cleaned_data   
       celular= celular (marca=datos.get ("marca"), modelo= datos.get ("modelo"))
       celular.save()
       return redirect ("celular")
    
   
    return render (request, "Crearcelular_2.html_2",{"formulario": formulario} )

def celular(request):
    
    Celular= Celular.objects.all ()
    
    
    return render (request,"celular", {"celular":celular})
