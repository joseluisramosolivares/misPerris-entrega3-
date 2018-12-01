from django.urls import path
from .views import listar_mascotas, agregar_mascota, modificar_mascota, eliminar_mascota

urlpatterns = [
    path('listar-mascota/', listar_mascotas, name="api_listar_mascotas"),
    path('agregar-mascota/', agregar_mascota, name="api_agregar_mascota"),
    path('modificar-mascota/', modificar_mascota, name="api_modificar_mascota"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="api_eliminar_mascota"),
]