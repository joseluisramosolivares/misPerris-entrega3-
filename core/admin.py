from django.contrib import admin
from .models import Mascota, Raza, Region, Ciudad, Postulante, Vivienda, Estado

class PostulanteAdmin(admin.ModelAdmin):
    list_display = ("run", "correo", "nombre")
    search_fields = ("run", "nombre")
    list_filter = ("run",)

class MascotaAdmin(admin.ModelAdmin):
    list_display = ("raza", "nombre")


admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Raza)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Postulante, PostulanteAdmin)
admin.site.register(Vivienda)
admin.site.register(Estado)

# Register your models here.
