from django.contrib import admin
from django.urls import path
from inicio import views
urlpatterns = [       
    path("",views.inicio, name= "inicio"),
    path("Crear/Celular_2/",views.crear_Celular_2 ,name="crear_Celular_2"),
    path("celulares/",views.celular, name= "celular")
]    