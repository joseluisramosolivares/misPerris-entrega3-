from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('listar/', listado, name="listado"),
    path('formulario/', formulario, name="formulario"),
    path('agregar/', agregar, name="agregar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('modificar/<id>/', modificar_mascota, name="modificar"),
    
]