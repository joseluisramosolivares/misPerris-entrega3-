from django.shortcuts import render, redirect
from .models import Mascota, Raza, Region, Ciudad, Postulante, Vivienda, Estado
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def listado(request):
    masco = Mascota.objects.all()
    return render(request,'core/listado_mascotas.html',{
        'mascotas': masco
    })

def formulario(request):
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()
    viviendas = Vivienda.objects.all()

    variables = {
        'regiones' : regiones,
        'ciudades' : ciudades,
        'viviendas' : viviendas
    }

    if request.POST:

        pos = Postulante()
        ciudad = Ciudad()

        pos.correo = request.POST.get('txtCorreo')
        pos.run = request.POST.get('txtRun')
        pos.nombre = request.POST.get('txtNombre')
        pos.fechanacimiento = request.POST.get('txtFechaNacimiento')
        pos.telefono = int(request.POST.get('txtTelefono'))

        #instancia de Region

        region = Region()
        region.id = int(request.POST.get('cboRegion'))
        #dejamos el objeto region dentro del postulante
        ciudad.regionid = region

        ciudad.id = int(request.POST.get('cboCiudad'))
        pos.ciudadid = ciudad

        vivienda = Vivienda()
        vivienda.id = int(request.POST.get('cboVivienda'))
        pos.viviendaid = vivienda


        try:
            pos.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/formulario.html',variables)


@login_required
def agregar(request):

    razas = Raza.objects.all()
    estados = Estado.objects.all()
    variables = {
        'razas':razas,
        'estados':estados
    }

    #preguntaremos si la peticion es POST
    if request.POST:
        #instanciar un Automovil
        masco = Mascota()
        masco.nombre = request.POST.get('txtNombre')
        masco.genero = request.POST.get('txtGenero')
        masco.fecha_ingreso = request.POST.get('txtFechaIngreso')
        masco.fecha_nacimiento = request.POST.get('txtFechaNacimiento')
        masco.descripcion = request.POST.get('txtDescripcion')
        masco.imagen = request.FILES.get('txtImagen')
        #instanciamos una Raza
        raza = Raza()
        raza.id = int(request.POST.get('cboRaza'))
        #dejamos el objeto marca dentro del auto
        masco.raza = raza
        #teniendo todos los datos capturados desde
        #el template, guardamos el automovil en la BBDD
        estado = Estado()
        estado.id = int(request.POST.get('cboEstado'))
        masco.estado = estado
        try:
            masco.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/agregar.html',variables)



def eliminar(request, id):

    #para eliminar es necesario primero buscar el automovil
    masco = Mascota.objects.get(id=id)

    #una vez encontrado el automovil se procede a eliminarlo
    try:
        masco.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje ="No se ha podido eliminar"
        messages.error(request, mensaje)
        
    #el redirect lo redirige por alias de una ruta
    return redirect(to="listado")


def modificar_mascota(request, id):
    razas = Raza.objects.all()
    estados = Estado.objects.all()

    masco = Mascota.objects.get(id=id)

    variables = {
        'masco':masco,
        'razas':razas,
        'estados':estados
    }

    if request.POST:

        masco = Mascota()
        masco.id = int(request.POST.get('txtId'))
        masco.nombre = request.POST.get('txtNombre')
        masco.genero = request.POST.get('txtGenero')
        masco.fecha_ingreso = request.POST.get('txtFechaIngreso')
        masco.fecha_nacimiento = request.POST.get('txtFechaNacimiento')
        masco.descripcion = request.POST.get('txtDescripcion')

        #objeto raza
        raza = Raza()
        raza.id = int(request.POST.get('cboRaza'))
        masco.raza = raza

        #objeto estados
        estado = Estado()
        estado.id = int(request.POST.get('cboEstado'))
        masco.estado = estado

        #se guarda

        try:
            masco.save()
            messages.success(request, "Actualizado correctamente")
        except:
            messages.error(request, "No se ha podido actualizar")
            
            #redirect para que mande al usuario al listado
        return redirect('listado')

    return render(request, 'core/modificar_mascota.html', variables)




