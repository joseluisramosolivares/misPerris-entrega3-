from django.db import models

# Create your models here.

class Raza(models.Model):
    nombre = models.CharField(max_length=50)
    #descripcion = models.CharField(max_length=200)
    #este str define el nombre
    #en los listados del admin
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas"

class Estado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero = models.CharField(max_length=50)
    fecha_ingreso = models.DateField(null=True)
    fecha_nacimiento = models.DateField(null=True)
    descripcion = models.CharField(max_length=200)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to="mascotas", null=True)

    def __str__(self):
        return self.nombre



class Region(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.id
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"

class Ciudad(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=50)
    regionid = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"


class Vivienda(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class Postulante(models.Model):
    correo = models.CharField(max_length=50)
    run = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=20)
    fechanacimiento = models.DateField(null=True)
    telefono = models.IntegerField(null=True)
    ciudadid = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    viviendaid = models.ForeignKey(Vivienda, on_delete=models.CASCADE)

    def __str__(self):
        return self.run
        
    
