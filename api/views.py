from django.shortcuts import render

#este paquete sirve para transformar
#objetos a json
from django.core import serializers
#este paquete nos permite devolver un json
#al usuario
from django.http import HttpResponse,HttpResponseBadRequest

import json

from core.models import Mascota, Raza, Region, Ciudad, Postulante, Vivienda, Estado

#este paquete nos permitira restringir un view a un determinado
#tipo http ya sea, get, post, put o delete
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
   
    mascotasJson = serializers.serialize('json', mascotas)

    #devolvemos el json al usuario
    return HttpResponse(mascotasJson, content_type="application/json")

@csrf_exempt
@require_http_methods(['POST'])
def agregar_mascota(request):
    body = request.body.decode('utf-8')

    #transformamos el body que esta en string a un diccionario
    #de python
    bodyDict = json.loads(body)

    #ahora procedemos a guardar un Automovil en la BBDD
    masco = Mascota()
    masco.nombre = bodyDict['nombre']
    masco.genero = bodyDict['genero']
    masco.fecha_ingreso = bodyDict['fecha_ingreso']
    masco.fecha_nacimiento = bodyDict['fecha_nacimiento']
    masco.descripcion = bodyDict['descripcion']
    masco.imagen = bodyDict['imagen']
    masco.raza = Raza(id=bodyDict['raza_id'])
    masco.estado = Estado(id=bodyDict['estado_id'])

    try:
        masco.save()
        return HttpResponse(json.dumps({'mensaje':'agregado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'error al agregar'}), content_type="application/json")


@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascota(request):
    body = request.body.decode('utf-8')

    #transformamos el body que esta en string a un diccionario
    #de python
    bodyDict = json.loads(body)

    #ahora procedemos a guardar una Mascota en la BBDD
    masco = Mascota()
    masco.id = bodyDict['id']
    masco.nombre = bodyDict['nombre']
    masco.genero = bodyDict['genero']
    masco.fecha_ingreso = bodyDict['fecha_ingreso']
    masco.fecha_nacimiento = bodyDict['fecha_nacimiento']
    masco.descripcion = bodyDict['descripcion']
    masco.imagen = bodyDict['imagen']
    masco.raza = Raza(id=bodyDict['raza_id'])
    masco.estado = Estado(id=bodyDict['estado_id'])

    try:
        masco.save()
        return HttpResponse(json.dumps({'mensaje':'modificado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'error al modificar'}), content_type="application/json")


@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascota(request, id):
    try:
        masco = Mascota.objects.get(id=id)
        masco.delete()
        return HttpResponse(json.dumps({'mensaje':'eliminado correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'error al eliminar'}), content_type="application/json")
    

